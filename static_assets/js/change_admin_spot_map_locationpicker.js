
	function updateControls(addressComponents) {
	    $('#id_address_street_name').val(addressComponents.streetName);
	    $('#id_address_street_number').val(addressComponents.streetNumber);
	    $('#id_address_town').val(addressComponents.city);
	    $('#id_address_postal_code').val(addressComponents.postalCode);
	    $('#id_address_country').val(addressComponents.country);
	}

	function updateLocation(lat, lng){
		// djangoPoint='Point('+lng+' '+lat+')';
		// $('#location').val(djangoPoint);
		console.log("executed");
		lat=lat.toFixed(5);
		lng=lng.toFixed(5);
		console.log(lat);
		console.log(lng);
		$('#id_latitude').val(lat);
		$('#id_longitude').val(lng);
	}



		$(document).ready(function() {

			$('#us3').locationpicker({
		        location: {latitude: $('#id_latitude').val(), longitude: $('#id_longitude').val()},
		        radius: 0,
		        inputBinding: {
		            // latitudeInput: $('#id_latitude'),
		            // longitudeInput: $('#id_longitude'),
		            locationNameInput: $('#us3-address')
		        },
		        enableAutocomplete: true,
		        onchanged: function (currentLocation, radius, isMarkerDropped) {
		            var addressComponents = $(this).locationpicker('map').location.addressComponents;
		            console.log(addressComponents);
		            console.log(currentLocation);
		            updateLocation(currentLocation.latitude, currentLocation.longitude);
		            updateControls(addressComponents);
		        },
		        oninitialized: function(component) {
		            // var addressComponents = $(component).locationpicker('map').location.addressComponents;
		            // updateControls(addressComponents);
		        }
		    });
		});