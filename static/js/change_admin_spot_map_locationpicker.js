
	function updateControls(addressComponents) {
	    $('#id_address_street').val(addressComponents.streetName);
	    $('#id_address_number').val(addressComponents.streetNumber);
	    $('#id_address_city').val(addressComponents.city);
	    $('#id_address_postal_code').val(addressComponents.postalCode);
	    $('#id_address_country').val(addressComponents.country);
	}

	function updateLocation(lat, lng){

		lat=lat.toFixed(5);
		lng=lng.toFixed(5);

		djangoPoint='Point('+lng+' '+lat+')';

		$('div.longitude .c-2 .grp-readonly').html(lng);
		$('div.latitude .c-2 .grp-readonly').html(lat);

		$('#id_location').val(djangoPoint)
	}



		$(document).ready(function() {
			latitude = Number.parseFloat($('div.latitude .c-2 .grp-readonly').text());
			longitude = Number.parseFloat($('div.longitude .c-2 .grp-readonly').text());
			if ( isNaN(latitude) || isNaN(longitude)) {
				latitude = 52.228378;
				longitude = 21.000447;
			}


			$('#us3').locationpicker({
		        location: {latitude: latitude, longitude: longitude},
		        radius: 0,
		        inputBinding: {
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