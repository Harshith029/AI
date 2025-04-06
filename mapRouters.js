const express = require('express');
const router = express.Router();
const mapsController = require('../controllers/mapsController');

// @route   GET api/maps/search
// @desc    Search for locations
// @access  Public
router.get('/search', mapsController.searchLocation);

// @route   GET api/maps/route
// @desc    Get route between two points
// @access  Public
router.get('/route', mapsController.getRoute);

// @route   GET api/maps/current-location
// @desc    Get address from coordinates
// @access  Public
router.get('/current-location', mapsController.getCurrentLocation);

module.exports = router;
