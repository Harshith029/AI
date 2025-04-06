const { geocode, reverseGeocode } = require('../services/geocodingService');
const { calculateRoute } = require('../services/routingService');

exports.searchLocation = async (req, res) => {
  try {
    const { query } = req.query;
    if (!query) {
      return res.status(400).json({ error: 'Search query is required' });
    }
    
    const result = await geocode(query);
    if (!result) {
      return res.status(404).json({ error: 'Location not found' });
    }
    
    res.json(result);
  } catch (error) {
    res.status(500).json({ error: 'Server error during search' });
  }
};

exports.getRoute = async (req, res) => {
  try {
    const { start, end } = req.query;
    
    if (!start || !end) {
      return res.status(400).json({ error: 'Both start and end points are required' });
    }
    
    // Geocode both addresses
    const startLocation = await geocode(start);
    const endLocation = await geocode(end);
    
    if (!startLocation || !endLocation) {
      return res.status(404).json({ error: 'Could not find one or both locations' });
    }
    
    // Calculate route
    const route = await calculateRoute(startLocation.coordinates, endLocation.coordinates);
    if (!route) {
      return res.status(404).json({ error: 'Could not calculate route' });
    }
    
    res.json({
      start: startLocation,
      end: endLocation,
      distance: route.distance,
      duration: route.duration,
      geometry: route.geometry
    });
  } catch (error) {
    res.status(500).json({ error: 'Server error during route calculation' });
  }
};

exports.getCurrentLocation = async (req, res) => {
  try {
    const { lat, lng } = req.query;
    
    if (!lat || !lng) {
      return res.status(400).json({ error: 'Both latitude and longitude are required' });
    }
    
    const location = await reverseGeocode(parseFloat(lat), parseFloat(lng));
    if (!location) {
      return res.status(404).json({ error: 'Location not found' });
    }
    
    res.json(location);
  } catch (error) {
    res.status(500).json({ error: 'Server error during reverse geocoding' });
  }
};
