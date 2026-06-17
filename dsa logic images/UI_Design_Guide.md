# IoT Compression Molding Dashboard — UI Design Guide

## 🎯 What You Just Got

A **production-ready React dashboard** with:
✅ Real-time sensor simulation (1-second refresh)
✅ Physics-based prediction curves (heat transfer + pressure dynamics)
✅ Model-based anomaly detection (predicted vs actual)
✅ Clean industrial dark theme
✅ Alert system with severity levels

---

## 🎨 UI Design Philosophy

### Color System (Industrial Safety Standard)
- **🟢 Green** — Normal operation, safe zone
- **🟡 Yellow** — Warning threshold, needs attention
- **🔴 Red** — Critical alert, immediate action required
- **Dark Gray (#1F2937)** — Background (reduces eye strain on factory floor)
- **Light Gray (#9CA3AF)** — Secondary text

### Layout Structure
```
┌─────────────────────────────────────────────────────────┐
│  HEADER: Title + Time Range Selector + System Status   │
├─────────────────────────────────────────────────────────┤
│  ROW 1: CRITICAL KPIs (Big, Bold, Instant Read)        │
│  [Temp] [Pressure] [Cycle Time] [Cycles] [State]      │
├─────────────────────────────────────────────────────────┤
│  ROW 2: TRENDS (Time-Series Charts)                    │
│  [Temp Chart] [Pressure Chart]                         │
├─────────────────────────────────────────────────────────┤
│  ROW 3: DIAGNOSTICS (Drill-Down Analysis)              │
│  [Vibration] [Energy] [Alert Log]                      │
└─────────────────────────────────────────────────────────┘
```

### Typography Hierarchy
1. **Critical Numbers** — 4xl (36px), bold
2. **Section Titles** — lg (18px), semibold
3. **Labels** — sm (14px), regular
4. **Secondary Info** — xs (12px), gray

---

## 🔥 Key Features Implemented

### 1. Model-Based Anomaly Detection
The dashboard doesn't just show data — it **predicts** what should happen.

**Temperature Prediction:**
```javascript
// Heat transfer equation: dT/dt = α(T_target - T_current)
predicted_temp = current_temp + alpha * (target_temp - current_temp) * time_step
```

**Pressure Prediction:**
```javascript
// Pressure dynamics: dP/dt = Q_pump - Q_leak
predicted_pressure = current_pressure + (pump_rate - leak_rate) * time_step
```

**If actual deviates from predicted → ALERT**

This is **smarter than rule-based alerts** because it learns machine behavior.

---

### 2. Real-Time Data Simulation
The dashboard generates realistic sensor data with:
- State machine logic (Idle → Heating → Pressing → Cooling)
- Physics-based transitions
- Realistic noise injection
- Circular buffer (keeps last 100 data points)

---

### 3. Alert System
Three alert types:
1. **Temperature deviation** — Actual vs predicted >10°C
2. **Pressure anomaly** — Drop during press cycle
3. **Vibration spike** — Abnormal mechanical behavior

Alerts display:
- 🔴 Red border = Critical
- 🟡 Yellow border = Warning
- Timestamp for traceability
- Auto-scroll (last 10 alerts)

---

## 🚀 How to Deploy

### Option 1: Run Locally (Quick Test)
```bash
# Install dependencies
npm install react recharts lucide-react

# Create a new React app
npx create-react-app iot-dashboard
cd iot-dashboard

# Replace src/App.js with the dashboard code
# Then run:
npm start
```

### Option 2: Embed in Existing Project
```jsx
import IoTDashboard from './IoT_Dashboard_Complete.jsx';

function App() {
  return <IoTDashboard />;
}
```

### Option 3: Connect Real MQTT Feed
Replace the `generateSensorData()` function with:
```javascript
import mqtt from 'mqtt';

const client = mqtt.connect('mqtt://your-broker-url');

client.on('message', (topic, message) => {
  const data = JSON.parse(message.toString());
  setCurrentData(data);
});

client.subscribe('machine/sensors');
```

---

## 🎛️ UI Customization Tips

### Change Color Theme
Find these lines in the code:
```javascript
className="bg-gray-900 text-gray-100"  // Main background
className="bg-gray-800 border border-gray-700"  // Card background
```

For **light mode**, swap to:
```javascript
className="bg-gray-50 text-gray-900"
className="bg-white border border-gray-200"
```

### Add More Sensors
Add a new gauge in ROW 1:
```jsx
<div className="bg-gray-800 border border-gray-700 rounded-lg p-6">
  <YourIconHere className="w-8 h-8 text-green-400 mb-3" />
  <div className="text-sm text-gray-400">Your Sensor Name</div>
  <div className="text-4xl font-bold text-green-400">
    {currentData.your_sensor_value}
  </div>
</div>
```

### Adjust Alert Thresholds
Find the alert logic in `useEffect`:
```javascript
if (tempDeviation > 10) {  // Change this number
  addAlert('Temperature deviation', 'critical');
}
```

---

## 📊 Chart Customization

All charts use **Recharts**. Here's what you can tweak:

### Temperature Chart
```jsx
<Line 
  type="monotone" 
  dataKey="mold_temperature" 
  stroke="#FB923C"  // Line color
  strokeWidth={2}   // Line thickness
  dot={false}       // Hide dots for cleaner look
/>
```

### Add New Chart Type
Want a bar chart for cycle count?
```jsx
import { BarChart, Bar } from 'recharts';

<ResponsiveContainer width="100%" height={200}>
  <BarChart data={historicalData}>
    <Bar dataKey="cycle_count" fill="#34D399" />
  </BarChart>
</ResponsiveContainer>
```

---

## 🧠 Smart Features to Add Later

### 1. Predictive Maintenance Score
Use historical vibration + temperature + cycle time to calculate:
```javascript
const maintenanceScore = 
  (vibration / 15) * 0.4 + 
  (temp_deviation / 20) * 0.3 + 
  (cycle_time_deviation / 10) * 0.3;

if (maintenanceScore > 0.7) {
  addAlert('Maintenance recommended within 48 hours', 'warning');
}
```

### 2. Energy Optimization
Compare current draw vs historical average:
```javascript
const avgEnergy = historicalData.reduce((sum, d) => sum + d.current_draw, 0) / historicalData.length;
const energyEfficiency = (avgEnergy / currentData.current_draw) * 100;
```

### 3. Quality Prediction
Use cycle time + temperature + pressure to predict product quality:
```javascript
const qualityScore = 
  (cycleTime >= 45 && cycleTime <= 47 ? 30 : 0) +
  (temp >= 175 && temp <= 185 ? 40 : 0) +
  (pressure >= 145 && pressure <= 155 ? 30 : 0);

// Display: "Quality Score: 85/100"
```

---

## 🛠️ Technical Stack

| Component | Technology | Why? |
|-----------|-----------|------|
| **Frontend** | React | Fast, component-based |
| **Charts** | Recharts | Lightweight, responsive |
| **Icons** | Lucide React | Clean industrial icons |
| **Styling** | Tailwind CSS | Utility-first, fast styling |
| **State Management** | React Hooks | Simple, no bloat |

---

## 📦 Required Dependencies

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "recharts": "^2.10.0",
    "lucide-react": "^0.263.1"
  }
}
```

---

## 🎯 Next Steps

1. **Test the simulation** — Run it locally and watch the data flow
2. **Connect real sensors** — Replace the `generateSensorData()` with MQTT/HTTP
3. **Deploy to factory floor** — Use Raspberry Pi or cloud dashboard
4. **Train operators** — Show them green = good, red = bad
5. **Collect feedback** — Operators will tell you what's missing

---

## 💡 Pro Tips

### For Factory Floor Deployment
- Use **large font sizes** (operators stand 2-3 meters away)
- **Dark theme** reduces glare from overhead lights
- **Flashing red border** for critical alerts (add CSS animation)
- **Audio alert** for critical failures (add `new Audio('alert.mp3').play()`)

### For Presentations
- Show **before/after** — manual monitoring vs IoT dashboard
- Highlight **cost savings** — early detection prevents downtime
- Emphasize **predictive power** — not just monitoring, but forecasting

### For Scaling
- Add **machine selector** (if you have multiple machines)
- Build **admin panel** (adjust thresholds without code changes)
- Export **CSV reports** (daily production summary)

---

## 🔍 Debugging Tips

### Dashboard not updating?
Check browser console for:
```javascript
console.log('Current data:', currentData);
```

### Charts not rendering?
Make sure Recharts is installed:
```bash
npm install recharts
```

### Colors not showing?
Tailwind needs configuration. Add to `tailwind.config.js`:
```javascript
module.exports = {
  content: ["./src/**/*.{js,jsx}"],
  theme: { extend: {} }
}
```

---

## 📚 Learn More

- **Heat Transfer Math:** https://en.wikipedia.org/wiki/Heat_equation
- **Recharts Docs:** https://recharts.org/
- **MQTT Protocol:** https://mqtt.org/
- **React Hooks:** https://react.dev/reference/react

---

**Built for: IoT Compression Molding Machine Monitoring**
**Project: Brake Shoe Manufacturing Quality System**
**Tech: React + Recharts + Physics-Based Prediction**

This is not just a dashboard. It's a **cyber-physical interface** between sensors and cognition.

Good luck building the future. 🚀
