const axios = require('axios');

// Using OSRM (Open Source Routing Machine) for route calculations
const calculateRoute = async (start, end) => {
  try {
    const response = await axios.get(
      `http://router.project-osrm.org/route/v1/driving/${start.lng},${start.lat};${end.lng},${end.lat}?overview=full&geometries=geojson`
    );
    
    if (response.data && response.data.routes && response.data.routes.length > 0) {
      const route = response.data.routes[0];
      return {
        distance: route.distance, // meters
        duration: route.duration, // seconds
        geometry: route.geometry
      };
    }
    return null;
  } catch (error) {
    console.error('Routing error:', error);
    throw error;
  }
};

module.exports = { calculateRoute };
