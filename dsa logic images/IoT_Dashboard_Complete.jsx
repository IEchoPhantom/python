import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, Area, AreaChart } from 'recharts';
import { Thermometer, Gauge, Clock, Activity, AlertTriangle, CheckCircle, Power, Zap } from 'lucide-react';

// Physics-based prediction model
const predictTemperature = (currentTemp, targetTemp, timeStep, alpha = 0.05) => {
  // Heat transfer: dT/dt = α(T_target - T_current)
  return currentTemp + alpha * (targetTemp - currentTemp) * timeStep;
};

const predictPressure = (currentPressure, targetPressure, timeStep, pumpRate = 0.1, leak = 0.02) => {
  // Pressure dynamics: dP/dt = Qpump - Qleak
  const pressureChange = (pumpRate * (targetPressure - currentPressure) - leak * currentPressure) * timeStep;
  return currentPressure + pressureChange;
};

// Simulated real-time data generator
const generateSensorData = (prevData) => {
  const machineStates = ['Idle', 'Heating', 'Pressing', 'Cooling'];
  const currentState = prevData?.machine_state || 'Idle';
  const stateIndex = machineStates.indexOf(currentState);
  
  // State machine logic
  let nextState = currentState;
  if (Math.random() > 0.95) {
    nextState = machineStates[(stateIndex + 1) % machineStates.length];
  }
  
  const targetTemp = nextState === 'Heating' || nextState === 'Pressing' ? 180 : 60;
  const targetPressure = nextState === 'Pressing' ? 150 : 10;
  
  const currentTemp = prevData?.mold_temperature || 25;
  const currentPressure = prevData?.hydraulic_pressure || 5;
  
  const temp = predictTemperature(currentTemp, targetTemp, 1);
  const pressure = predictPressure(currentPressure, targetPressure, 1);
  
  // Add realistic noise
  const tempNoise = (Math.random() - 0.5) * 3;
  const pressureNoise = (Math.random() - 0.5) * 5;
  
  return {
    timestamp: new Date().toLocaleTimeString(),
    mold_temperature: Math.max(25, Math.min(200, temp + tempNoise)),
    hydraulic_pressure: Math.max(0, Math.min(200, pressure + pressureNoise)),
    cycle_time: nextState === 'Pressing' ? Math.random() * 2 + 45 : 0,
    cycle_count: (prevData?.cycle_count || 0) + (nextState === 'Cooling' && prevData?.machine_state === 'Pressing' ? 1 : 0),
    machine_state: nextState,
    vibration: Math.random() * 10 + (nextState === 'Pressing' ? 5 : 0),
    current_draw: nextState === 'Pressing' ? 25 + Math.random() * 5 : 5 + Math.random() * 2,
    predicted_temp: predictTemperature(currentTemp, targetTemp, 1),
    predicted_pressure: predictPressure(currentPressure, targetPressure, 1)
  };
};

export default function IoTDashboard() {
  const [currentData, setCurrentData] = useState(generateSensorData());
  const [historicalData, setHistoricalData] = useState([]);
  const [alerts, setAlerts] = useState([]);
  const [timeRange, setTimeRange] = useState('1h');
  
  useEffect(() => {
    const interval = setInterval(() => {
      const newData = generateSensorData(currentData);
      setCurrentData(newData);
      
      setHistoricalData(prev => {
        const updated = [...prev, newData].slice(-100); // Keep last 100 points
        return updated;
      });
      
      // Model-based anomaly detection
      const tempDeviation = Math.abs(newData.mold_temperature - newData.predicted_temp);
      const pressureDeviation = Math.abs(newData.hydraulic_pressure - newData.predicted_pressure);
      
      if (tempDeviation > 10) {
        addAlert('Temperature deviation from predicted model', 'critical', newData.timestamp);
      }
      
      if (pressureDeviation > 15 && newData.machine_state === 'Pressing') {
        addAlert('Pressure anomaly detected during press cycle', 'warning', newData.timestamp);
      }
      
      if (newData.mold_temperature > 190) {
        addAlert('Temperature exceeds safe operating limit', 'critical', newData.timestamp);
      }
      
      if (newData.vibration > 12) {
        addAlert('Abnormal vibration detected', 'warning', newData.timestamp);
      }
      
    }, 1000);
    
    return () => clearInterval(interval);
  }, [currentData]);
  
  const addAlert = (message, severity, timestamp) => {
    setAlerts(prev => {
      const newAlert = { message, severity, timestamp, id: Date.now() };
      return [newAlert, ...prev].slice(0, 10); // Keep last 10 alerts
    });
  };
  
  const getStatusColor = (state) => {
    const colors = {
      'Idle': 'bg-gray-500',
      'Heating': 'bg-yellow-500',
      'Pressing': 'bg-green-500',
      'Cooling': 'bg-blue-500'
    };
    return colors[state] || 'bg-gray-500';
  };
  
  const getTempColor = (temp) => {
    if (temp < 150) return 'text-green-400';
    if (temp < 180) return 'text-yellow-400';
    return 'text-red-400';
  };
  
  const getPressureColor = (pressure) => {
    if (pressure < 100) return 'text-green-400';
    if (pressure < 160) return 'text-yellow-400';
    return 'text-red-400';
  };

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 p-6">
      {/* Header */}
      <div className="mb-6 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-white">Compression Molding Monitor</h1>
          <p className="text-gray-400 text-sm mt-1">Real-time IoT Dashboard · Brake Shoe Manufacturing</p>
        </div>
        <div className="flex gap-4 items-center">
          <select 
            value={timeRange} 
            onChange={(e) => setTimeRange(e.target.value)}
            className="bg-gray-800 border border-gray-700 rounded px-4 py-2 text-sm"
          >
            <option value="1h">Last 1 Hour</option>
            <option value="4h">Last 4 Hours</option>
            <option value="24h">Last 24 Hours</option>
          </select>
          <div className="flex items-center gap-2 px-4 py-2 bg-green-900/30 border border-green-500/50 rounded">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            <span className="text-green-400 text-sm font-medium">System Online</span>
          </div>
        </div>
      </div>

      {/* ROW 1: Critical KPIs */}
      <div className="grid grid-cols-5 gap-4 mb-6">
        {/* Temperature Gauge */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6 flex flex-col items-center justify-center">
          <Thermometer className="w-8 h-8 text-orange-400 mb-3" />
          <div className="text-sm text-gray-400 mb-1">Mold Temperature</div>
          <div className={`text-4xl font-bold ${getTempColor(currentData.mold_temperature)}`}>
            {currentData.mold_temperature.toFixed(1)}°C
          </div>
          <div className="text-xs text-gray-500 mt-2">Target: 180°C</div>
        </div>

        {/* Pressure Gauge */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6 flex flex-col items-center justify-center">
          <Gauge className="w-8 h-8 text-blue-400 mb-3" />
          <div className="text-sm text-gray-400 mb-1">Hydraulic Pressure</div>
          <div className={`text-4xl font-bold ${getPressureColor(currentData.hydraulic_pressure)}`}>
            {currentData.hydraulic_pressure.toFixed(0)} bar
          </div>
          <div className="text-xs text-gray-500 mt-2">Nominal: 150 bar</div>
        </div>

        {/* Cycle Time */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6 flex flex-col items-center justify-center">
          <Clock className="w-8 h-8 text-purple-400 mb-3" />
          <div className="text-sm text-gray-400 mb-1">Current Cycle Time</div>
          <div className="text-4xl font-bold text-purple-400">
            {currentData.cycle_time > 0 ? currentData.cycle_time.toFixed(1) : '--'}s
          </div>
          <div className="text-xs text-gray-500 mt-2">Target: 45-47s</div>
        </div>

        {/* Total Cycles */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6 flex flex-col items-center justify-center">
          <Activity className="w-8 h-8 text-cyan-400 mb-3" />
          <div className="text-sm text-gray-400 mb-1">Cycles Completed</div>
          <div className="text-4xl font-bold text-cyan-400">
            {currentData.cycle_count}
          </div>
          <div className="text-xs text-gray-500 mt-2">Today's production</div>
        </div>

        {/* Machine State */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6 flex flex-col items-center justify-center">
          <Power className="w-8 h-8 text-white mb-3" />
          <div className="text-sm text-gray-400 mb-1">Machine State</div>
          <div className={`px-4 py-2 rounded-full font-bold text-lg ${getStatusColor(currentData.machine_state)} mt-2`}>
            {currentData.machine_state}
          </div>
        </div>
      </div>

      {/* ROW 2: Trend Charts */}
      <div className="grid grid-cols-2 gap-4 mb-6">
        {/* Temperature Trend with Prediction */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Thermometer className="w-5 h-5 text-orange-400" />
            Temperature Trend vs Predicted
          </h2>
          <ResponsiveContainer width="100%" height={250}>
            <LineChart data={historicalData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
              <XAxis dataKey="timestamp" stroke="#9CA3AF" tick={{ fontSize: 11 }} />
              <YAxis stroke="#9CA3AF" tick={{ fontSize: 11 }} domain={[0, 200]} />
              <Tooltip contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }} />
              <Legend />
              <Line type="monotone" dataKey="mold_temperature" stroke="#FB923C" strokeWidth={2} dot={false} name="Actual Temp" />
              <Line type="monotone" dataKey="predicted_temp" stroke="#FBBF24" strokeWidth={2} strokeDasharray="5 5" dot={false} name="Predicted Temp" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* Pressure Trend with Prediction */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Gauge className="w-5 h-5 text-blue-400" />
            Pressure Trend vs Predicted
          </h2>
          <ResponsiveContainer width="100%" height={250}>
            <LineChart data={historicalData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
              <XAxis dataKey="timestamp" stroke="#9CA3AF" tick={{ fontSize: 11 }} />
              <YAxis stroke="#9CA3AF" tick={{ fontSize: 11 }} domain={[0, 200]} />
              <Tooltip contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }} />
              <Legend />
              <Line type="monotone" dataKey="hydraulic_pressure" stroke="#60A5FA" strokeWidth={2} dot={false} name="Actual Pressure" />
              <Line type="monotone" dataKey="predicted_pressure" stroke="#34D399" strokeWidth={2} strokeDasharray="5 5" dot={false} name="Predicted Pressure" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* ROW 3: Diagnostics */}
      <div className="grid grid-cols-3 gap-4">
        {/* Vibration Chart */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Activity className="w-5 h-5 text-red-400" />
            Vibration Level
          </h2>
          <ResponsiveContainer width="100%" height={200}>
            <AreaChart data={historicalData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
              <XAxis dataKey="timestamp" stroke="#9CA3AF" tick={{ fontSize: 11 }} />
              <YAxis stroke="#9CA3AF" tick={{ fontSize: 11 }} />
              <Tooltip contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }} />
              <Area type="monotone" dataKey="vibration" stroke="#F87171" fill="#EF4444" fillOpacity={0.3} />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        {/* Energy Consumption */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Zap className="w-5 h-5 text-yellow-400" />
            Current Draw (Energy)
          </h2>
          <ResponsiveContainer width="100%" height={200}>
            <AreaChart data={historicalData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
              <XAxis dataKey="timestamp" stroke="#9CA3AF" tick={{ fontSize: 11 }} />
              <YAxis stroke="#9CA3AF" tick={{ fontSize: 11 }} />
              <Tooltip contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }} />
              <Area type="monotone" dataKey="current_draw" stroke="#FBBF24" fill="#F59E0B" fillOpacity={0.3} />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        {/* Alert Log */}
        <div className="bg-gray-800 border border-gray-700 rounded-lg p-6">
          <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <AlertTriangle className="w-5 h-5 text-yellow-400" />
            Alert Log
          </h2>
          <div className="space-y-2 max-h-[200px] overflow-y-auto">
            {alerts.length === 0 ? (
              <div className="flex items-center gap-2 text-green-400 text-sm">
                <CheckCircle className="w-4 h-4" />
                All systems normal
              </div>
            ) : (
              alerts.map(alert => (
                <div key={alert.id} className={`p-2 rounded text-xs border-l-4 ${
                  alert.severity === 'critical' 
                    ? 'bg-red-900/20 border-red-500' 
                    : 'bg-yellow-900/20 border-yellow-500'
                }`}>
                  <div className="font-semibold">{alert.message}</div>
                  <div className="text-gray-400 text-[10px] mt-1">{alert.timestamp}</div>
                </div>
              ))
            )}
          </div>
        </div>
      </div>

      {/* Footer Info */}
      <div className="mt-6 text-center text-xs text-gray-500">
        Model-based anomaly detection active · Heat transfer equation: ∂T/∂t = α∇²T · Pressure dynamics: dP/dt = Q<sub>pump</sub> - Q<sub>leak</sub>
      </div>
    </div>
  );
}
