

$( document ).ready(function() {

   $('#movie_list_refresh').click(function(){
        get_movies_list();
   });

   get_movies_list();

});

function get_movies_list(){
    $.ajax({
      url: 'get_movies_list',
      type: "POST",
      data: "",
      dataType: 'html',

      beforeSend: function() {
            var html = '<div class="loader" id="load"></div>';
            $('#movies_list').append(html);
          },
      success: function(result) {
            $('#load').remove();
            $('#movies_list').empty();
            $('#movies_list').append(result);
        },

   });
}

function get_cheap_price(provider_details, detail_index){
    $.ajax({
      url: 'get_cheap_price',
      type: "POST",
      data: JSON.stringify({"Providers": provider_details}),
      contentType: 'application/json;charset=UTF-8',
      dataType: 'json',

      success: function(result) {
            $("#wait_loader_"+detail_index).hide();
            var movie_details = result;

            if (movie_details != undefined && movie_details.hasOwnProperty('Details')){

                $("#price_"+detail_index).text("$"+movie_details["Price"]);

                poster_src = movie_details['Details'].hasOwnProperty('Poster')?movie_details['Details']['Poster']:'';
                $("#modal_poster_"+detail_index).html("<img src="+poster_src+" class='img-thumbnail' >");
                $("#country_"+detail_index).text(movie_details['Details'].hasOwnProperty('Country')?movie_details['Details']['Country']:"-");
                $("#rated_"+detail_index).text(movie_details['Details'].hasOwnProperty('Rated')?movie_details['Details']['Rated']:"-");

                rating =  movie_details['Details'].hasOwnProperty('Rating')?movie_details['Details']['Rating']:"-";
                votes = movie_details['Details'].hasOwnProperty('Votes')?movie_details['Details']['Votes']:"-";
                rating_votes = rating+"/10 ("+votes+")";

                $("#rating_votes_"+detail_index).text(rating_votes);
                $("#language_"+detail_index).text(movie_details['Details'].hasOwnProperty('Language')?movie_details['Details']['Language']:"-");
                $("#released_"+detail_index).text(movie_details['Details'].hasOwnProperty('Released')?movie_details['Details']['Released']:"-");
                $("#runtime_"+detail_index).text(movie_details['Details'].hasOwnProperty('Runtime')?movie_details['Details']['Runtime']:"-");
                $("#genre_"+detail_index).text(movie_details['Details'].hasOwnProperty('Genre')?movie_details['Details']['Genre']:"-");
                $("#metascore_"+detail_index).text(movie_details['Details'].hasOwnProperty('Metascore')?movie_details['Details']['Metascore']:"-");

                $("#director_"+detail_index).text(movie_details['Details'].hasOwnProperty('Director')?movie_details['Details']['Director']:"-");
                $("#writer_"+detail_index).text(movie_details['Details'].hasOwnProperty('Writer')?movie_details['Details']['Writer']:"");
                $("#actors_"+detail_index).text(movie_details['Details'].hasOwnProperty('Actors')?movie_details['Details']['Actors']:"-");
                $("#plot_"+detail_index).text(movie_details['Details'].hasOwnProperty('Plot')?movie_details['Details']['Plot']:"-");
                $("#awards_"+detail_index).text(movie_details['Details'].hasOwnProperty('Awards')?movie_details['Details']['Awards']:"-");

            }
        },
   });
}