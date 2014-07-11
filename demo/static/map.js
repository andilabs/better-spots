var opts = {
  lines: 13, // The number of lines to draw
  length: 29, // The length of each line
  width: 10, // The line thickness
  radius: 26, // The radius of the inner circle
  corners: 0.7, // Corner roundness (0..1)
  rotate: 0, // The rotation offset
  direction: 1, // 1: clockwise, -1: counterclockwise
  color: '#000', // #rgb or #rrggbb or array of colors
  speed: 1.6, // Rounds per second
  trail: 72, // Afterglow percentage
  shadow: false, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: '300%', // Top position relative to parent
  left: '50%' // Left position relative to parent
};


var target = document.getElementById('spots_list');
var spinner = new Spinner(opts).spin(target);

$.cookie("example", "foo", { expires: 7 });

var arrMarkers = {};


function initialize() {

$('#map_canvas').gmap().bind('init', function(evt, map) {


  $('#map_canvas').gmap('getCurrentPosition', function(position, status) {
    if ( status === 'OK' ) {
      var clientPosition = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);



      var ikonka = new google.maps.MarkerImage('http://127.0.0.1:8000/static/lapka_icon.png',  new google.maps.Size(50, 50), new google.maps.Point(0,0), new google.maps.Point(0, 50));

      $('#map_canvas').gmap('addMarker', {'position': clientPosition,'zoom':3, 'bounds': true,'icon':ikonka}).click(function() {

        $('#map_canvas').gmap('openInfoWindow', { 'content': "<h2>You!</h2>" }, this);
      });




$('#map_canvas').gmap('option','zoom',15);

    }
else{
  $('#map_canvas').gmap('option','zoom',3);
}
 var pair_mark = {}
  var url = '/http://127.0.0.1:8000/static/spots_mockup.json'
  console.log(url);
  var jqxhr = $.getJSON('http://127.0.0.1:8000/static/spots_mockup.json', function(data) { 

    $.each( data, function(i, marker) {

            box = "<a href='#' class='list-group-item' id="+marker.id+"><h4 class='list-group-item-heading'>"+marker.name+"</h4><p class='list-group-item-text'>"+marker.address_street+" "+marker.address_number+"<span class='spot_item_details' style='display:none' id="+marker.id+"><br><span class='glyphicon glyphicon-phone-alt'></span> "+marker.phone_number+"<i class='fa fa-facebook'></i></span></p></a>"

          $("#spots_list").append(box);


           var labelka = "#spot"+marker.id
           var contencik = $('<div class="spot_info" id='+marker.id+'><h4>'+marker.name+'</h4><br>'+marker.address_street+' '+marker.address_number+'</div>').append($('<div id="spot'+marker.id+'" class="rate"></div>')
                              .raty({readOnly:true, score:marker.friendly_rate})
                              )[0];

           pair_mark[labelka]=marker.friendly_rate

           if (marker.is_accepted==false){
            marker.dogs_allowed ='dog_undefined_allowed'
           }
           icony_allowed = {true:'http://127.0.0.1:8000/static/dog_allowed.png',false:'http://127.0.0.1:8000/static/dog_not_allowed.png','dog_undefined_allowed':'http://127.0.0.1:8000/static/dog_undefined_allowed.png'}

           var SpotIcon = new google.maps.MarkerImage(icony_allowed[marker.dogs_allowed], null,  new google.maps.Point(0, 0), new google.maps.Point(0, 0));


            var SpotMarker = new google.maps.Marker({
                position: new google.maps.LatLng(marker.latitude, marker.longitude),
                bounds: false ,
                icon: SpotIcon
            });

            var SpotInfoWindow = new google.maps.InfoWindow({
              content: contencik
            });
            arrMarkers[marker.id] = {'marker': SpotMarker, 'info_window': SpotInfoWindow};

            $('#map_canvas').gmap('addMarker', SpotMarker).click(function() {
              $('#map_canvas').gmap('openInfoWindow', SpotInfoWindow, this);
              $('#map_canvas').gmap('get', 'map').panTo(this.getPosition());
              
              idik = '#'+$(contencik).attr('id');
              $('#spots_list a').each(function( index ) {
               $( this ).removeClass('active');
               $(this).find('p span.spot_item_details').attr('style','display:none');
              });
              $('#spots_list').find(idik).focus().attr('class','list-group-item active');
              $('#spots_list p').find('span'+idik).attr('style','display:block');
            });
    });
  });
spinner.stop();

  // $('#map_canvas').fadeIn();

 $("#map_canvas").animate({"opacity": "1.0"}, "slow");




  });
});



}
$('#spots_list').on("click", 'a.list-group-item', function(evt) {

  $('#spots_list a').each(function( index ) {
     $( this ).removeClass('active');
     $(this).find('p span.spot_item_details').attr('style','display:none');
  });

  idik = $(this).attr('id');
  $('#spots_list').find('#'+idik).focus().attr('class','list-group-item active');
  $('#spots_list p').find('span#'+idik).attr('style','display:block');


  $('#map_canvas').gmap('openInfoWindow',arrMarkers[idik].info_window, arrMarkers[idik].marker);//,
  $('#map_canvas').gmap('get', 'map').panTo(arrMarkers[idik].marker.getPosition());

});
