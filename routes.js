const mongoose = require('mongoose');

const RouteSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  startPoint: {
    name: String,
    coordinates: {
      lat: Number,
      lng: Number
    }
  },
  endPoint: {
    name: String,
    coordinates: {
      lat: Number,
      lng: Number
    }
  },
  waypoints: [{
    name: String,
    coordinates: {
      lat: Number,
      lng: Number
    }
  }],
  distance: Number, // in meters
  duration: Number, // in seconds
  createdAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = mongoose.model('Route', RouteSchema);
