const axios = require('axios');

// Using OpenStreetMap Nominatim API for geocoding
const geocode = async (address) => {
  try {
    const response = await axios.get('https://nominatim.openstreetmap.org/search', {
      params: {
        q: address,
        format: 'json',
        limit: 1
      }
    });
    
    if (response.data && response.data.length > 0) {
      return {
        name: address,
        address: response.data[0].display_name,
        coordinates: {
          lat: parseFloat(response.data[0].lat),
          lng: parseFloat(response.data[0].lon)
        }
      };
    }
    return null;
  } catch (error) {
    console.error('Geocoding error:', error);
    throw error;
  }
};

const reverseGeocode = async (lat, lng) => {
  try {
    const response = await axios.get('https://nominatim.openstreetmap.org/reverse', {
      params: {
        lat,
        lon: lng,
        format: 'json'
      }
    });
    
    if (response.data) {
      return {
        name: response.data.display_name.split(',')[0],
        address: response.data.display_name,
        coordinates: { lat, lng }
      };
    }
    return null;
  } catch (error) {
    console.error('Reverse geocoding error:', error);
    throw error;
  }
};

module.exports = { geocode, reverseGeocode };
