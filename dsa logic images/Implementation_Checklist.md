# IoT Dashboard — Implementation Checklist

## ✅ Phase 1: Local Testing (Week 1)

### Day 1-2: Setup Environment
- [ ] Install Node.js (v16 or higher)
- [ ] Create React app: `npx create-react-app iot-dashboard`
- [ ] Install dependencies:
  ```bash
  npm install recharts lucide-react
  npm install -D tailwindcss postcss autoprefixer
  npx tailwindcss init -p
  ```
- [ ] Copy the dashboard code from `IoT_Dashboard_Complete.jsx`
- [ ] Run locally: `npm start`
- [ ] Verify dashboard loads with simulated data

### Day 3-4: Customize for Your Machine
- [ ] Update temperature ranges (currently 0-200°C)
- [ ] Update pressure ranges (currently 0-200 bar)
- [ ] Adjust alert thresholds:
  - Temperature deviation: Currently >10°C
  - Pressure drop: Currently >15 bar
  - Vibration spike: Currently >12 units
- [ ] Add your company logo/branding
- [ ] Test on different screen sizes (factory floor displays are usually 1920x1080)

### Day 5-7: Test Edge Cases
- [ ] Simulate machine failure (extreme values)
- [ ] Test alert system (verify colors, sounds)
- [ ] Check performance (should handle 1000+ data points smoothly)
- [ ] Get feedback from operators (UI/UX improvements)

---

## ✅ Phase 2: Hardware Integration (Week 2-3)

### Sensor Setup
- [ ] Mount temperature sensor (thermocouple/PT100)
- [ ] Mount pressure sensor (hydraulic line tap)
- [ ] Install proximity switches (cycle detection)
- [ ] Optional: Vibration sensor, current clamp
- [ ] Test sensor readings with multimeter

### Microcontroller Programming
- [ ] Choose ESP32 or Raspberry Pi
- [ ] Write sensor reading code (Python/Arduino)
- [ ] Implement MQTT publishing:
  ```python
  import paho.mqtt.client as mqtt
  import json
  
  client = mqtt.Client()
  client.connect("mqtt-broker-url", 1883)
  
  data = {
      "machine_id": "M001",
      "timestamp": datetime.now().isoformat(),
      "mold_temperature": sensor.read_temp(),
      "hydraulic_pressure": sensor.read_pressure()
  }
  
  client.publish("machine/sensors", json.dumps(data))
  ```
- [ ] Test MQTT publish (use MQTT Explorer to verify)
- [ ] Set publish interval to 1 second

### Dashboard Backend
- [ ] Set up MQTT broker (Mosquitto or cloud MQTT)
- [ ] Replace `generateSensorData()` with MQTT subscription:
  ```javascript
  import mqtt from 'mqtt';
  
  const client = mqtt.connect('mqtt://your-broker');
  
  client.on('connect', () => {
    client.subscribe('machine/sensors');
  });
  
  client.on('message', (topic, message) => {
    const data = JSON.parse(message.toString());
    setCurrentData(data);
  });
  ```
- [ ] Test real-time data flow
- [ ] Verify predictions match actual machine behavior

---

## ✅ Phase 3: Database & Storage (Week 4)

### Time-Series Database
- [ ] Choose database:
  - **InfluxDB** (recommended for IoT)
  - **TimescaleDB** (PostgreSQL extension)
  - **AWS Timestream** (cloud option)
  
- [ ] Install InfluxDB:
  ```bash
  docker run -p 8086:8086 influxdb:latest
  ```

- [ ] Store data:
  ```python
  from influxdb_client import InfluxDBClient, Point
  
  client = InfluxDBClient(url="http://localhost:8086", token="your-token")
  write_api = client.write_api()
  
  point = Point("machine_data") \
      .tag("machine_id", "M001") \
      .field("temperature", data['mold_temperature']) \
      .field("pressure", data['hydraulic_pressure'])
  
  write_api.write(bucket="sensors", record=point)
  ```

- [ ] Query historical data for charts
- [ ] Set retention policy: 24h hot, 1 year cold

### Alert System
- [ ] Set up email notifications (use Nodemailer):
  ```javascript
  const nodemailer = require('nodemailer');
  
  const sendAlert = (message) => {
    transporter.sendMail({
      from: 'iot@factory.com',
      to: 'operator@factory.com',
      subject: 'CRITICAL: Machine Alert',
      text: message
    });
  };
  ```
  
- [ ] Optional: SMS alerts (Twilio)
- [ ] Optional: Push notifications (Firebase)
- [ ] Test all alert channels

---

## ✅ Phase 4: Deployment (Week 5)

### Option A: Local Factory Server
- [ ] Set up Raspberry Pi 4 (8GB RAM)
- [ ] Install Ubuntu Server
- [ ] Install Node.js, MQTT, InfluxDB
- [ ] Deploy dashboard (PM2 for process management)
- [ ] Connect to factory network
- [ ] Set static IP address
- [ ] Configure firewall (only allow factory network)

### Option B: Cloud Deployment
- [ ] Choose platform (AWS, Azure, Google Cloud)
- [ ] Set up EC2 instance (t3.medium recommended)
- [ ] Configure security groups
- [ ] Deploy dashboard using Docker:
  ```dockerfile
  FROM node:18
  WORKDIR /app
  COPY package.json .
  RUN npm install
  COPY . .
  RUN npm run build
  EXPOSE 3000
  CMD ["npm", "start"]
  ```
- [ ] Set up domain name (optional)
- [ ] Enable HTTPS (Let's Encrypt)

### Display Setup
- [ ] Mount 24" or 32" monitor near machine
- [ ] Set to auto-start dashboard on boot
- [ ] Adjust brightness for factory lighting
- [ ] Test visibility from 3 meters away
- [ ] Lock down browser (kiosk mode)

---

## ✅ Phase 5: Training & Documentation (Week 6)

### Operator Training
- [ ] Create user manual (PDF)
- [ ] Record video tutorial (5-10 minutes)
- [ ] Train operators on:
  - What each gauge means
  - How to read charts
  - When to take action on alerts
  - Who to call for critical alerts
- [ ] Create quick reference card (laminated, near machine)

### Maintenance Documentation
- [ ] Document sensor calibration procedure
- [ ] Create troubleshooting guide:
  - Dashboard not updating → Check MQTT connection
  - Wrong readings → Calibrate sensors
  - Slow performance → Clear old data
- [ ] Schedule weekly system health check
- [ ] Set up automated backups

---

## ✅ Phase 6: Optimization (Ongoing)

### Performance Tuning
- [ ] Monitor dashboard load time (should be <2 seconds)
- [ ] Optimize chart rendering (use data downsampling for old data)
- [ ] Set up performance monitoring (Google Analytics or custom)
- [ ] Profile memory usage (should stay <500MB)

### Model Improvement
- [ ] Collect 1 month of data
- [ ] Analyze prediction accuracy:
  - Temperature prediction error
  - Pressure prediction error
- [ ] Tune alpha parameter in heat transfer model
- [ ] Adjust pump rate and leak rate in pressure model
- [ ] Add machine learning (optional):
  ```python
  from sklearn.ensemble import RandomForestRegressor
  
  # Train on historical data
  model = RandomForestRegressor()
  model.fit(X_train, y_train)
  
  # Predict next temperature
  predicted_temp = model.predict(current_features)
  ```

### Feature Additions
- [ ] Predictive maintenance score (based on vibration + cycle time)
- [ ] Energy efficiency dashboard
- [ ] Production quality metrics
- [ ] Shift-wise performance comparison
- [ ] Export daily/weekly reports (PDF/Excel)
- [ ] Mobile app version (React Native)

---

## 📊 Success Metrics

### Technical KPIs
- ✅ Dashboard uptime: >99.5%
- ✅ Data latency: <2 seconds
- ✅ Alert accuracy: >95%
- ✅ False positive rate: <5%

### Business KPIs
- ✅ Reduce unplanned downtime by 30%
- ✅ Improve product quality (reduce defects by 20%)
- ✅ Decrease energy consumption by 15%
- ✅ Increase operator efficiency by 25%

---

## 🚨 Common Pitfalls & Solutions

### Problem: Dashboard not updating
**Solution:** Check MQTT connection, verify broker is running

### Problem: Sensor readings are noisy
**Solution:** Add moving average filter:
```javascript
const smoothedTemp = historicalData.slice(-5)
  .reduce((sum, d) => sum + d.mold_temperature, 0) / 5;
```

### Problem: Alerts are too frequent
**Solution:** Add debouncing:
```javascript
let alertTimeout;
const addAlert = (message) => {
  clearTimeout(alertTimeout);
  alertTimeout = setTimeout(() => {
    // Add alert only if condition persists for 5 seconds
    setAlerts(prev => [message, ...prev]);
  }, 5000);
};
```

### Problem: Charts are slow
**Solution:** Downsample old data:
```javascript
const downsample = (data, factor) => {
  return data.filter((_, i) => i % factor === 0);
};
```

---

## 🔐 Security Checklist

- [ ] Change default MQTT passwords
- [ ] Use TLS for MQTT (not plain TCP)
- [ ] Set up firewall rules (only factory network)
- [ ] Enable dashboard authentication (login required)
- [ ] Encrypt data at rest (InfluxDB encryption)
- [ ] Regular security audits
- [ ] Backup encryption keys securely

---

## 📞 Support & Resources

### If Dashboard Breaks
1. Check browser console for errors (F12)
2. Verify MQTT broker is running: `systemctl status mosquitto`
3. Check database connection: `influx ping`
4. Restart services: `pm2 restart all`

### Need Help?
- **React Issues:** https://react.dev/
- **MQTT Issues:** https://mqtt.org/
- **InfluxDB Issues:** https://docs.influxdata.com/
- **Hardware Issues:** ESP32 forum / Raspberry Pi forum

---

## 🎯 Final Thoughts

This dashboard is not just monitoring. It's a **cyber-physical interface**.

You're translating:
- **Physics** (heat transfer, pressure dynamics) → **Math** (differential equations)
- **Math** → **Data** (sensor readings)
- **Data** → **Cognition** (visual dashboard)
- **Cognition** → **Action** (operator decisions)

That's the future of manufacturing. Good luck building it. 🚀

---

**Project:** IoT Compression Molding Machine Monitoring
**Industry:** Brake Shoe Manufacturing
**Status:** Ready for Implementation
**Estimated ROI:** 6-12 months
