require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const jobworkRoutes = require('./routes/jobworkRoutes');

const app = express();
app.use(cors());
app.use(express.json());

const MONGO_URI = process.env.MONGO_URI || 'mongodb://127.0.0.1:27017/madzinu_audit_db';

mongoose.connect(MONGO_URI)
    .then(() => console.log('✅ MongoDB Audit Database Connected Successfully'))
    .catch(err => console.error('❌ Database Connection Error:', err));

app.use('/api/v1/jobwork', jobworkRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Enterprise Audit Server running on port ${PORT}`));
