$(document).ready(function(){
    $.getJSON("https://apicovid19indonesia-v2.vercel.app/api/indonesia", 
    function(data){
        $('#jumlah_positif').text(data.positif);
        $('#jumlah_sembuh').text(data.sembuh);
        $('#jumlah_meninggal').text(data.meninggal);
    });
});