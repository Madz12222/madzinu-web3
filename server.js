import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import dotenv from 'dotenv';
import jobworkRoutes from './routes/jobworkRoutes.js';

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from public directory
app.use(express.static('public'));

// Connect to MongoDB
if (process.env.MONGO_URI) {
    mongoose.connect(process.env.MONGO_URI)
        .then(() => console.log('✅ MongoDB connected successfully'))
        .catch(err => console.error('❌ MongoDB connection error:', err));
}

// API Routes
app.use('/api', jobworkRoutes);

// Root route fallback
app.get('/', (req, res) => {
    res.sendFile('index.html', { root: 'public' });
});

// Only listen locally if not running on Vercel serverless
if (process.env.NODE_ENV !== 'production') {
    const PORT = process.env.PORT || 5000;
    app.listen(PORT, () => {
        console.log(`🚀 Madzinu Web3 Server running successfully on port ${PORT}`);
    });
}

export default app;
