$(document).ready(function(){
    $("#prov_container").hide();

    $.getJSON("https://apicovid19indonesia-v2.vercel.app/api/indonesia", 
    function(data){
        $('#jumlah_positif').text(data.positif);
        $('#jumlah_sembuh').text(data.sembuh);
        $('#jumlah_meninggal').text(data.meninggal);
    });

    $.getJSON("http://apicovid19indonesia-v2.vercel.app/api/indonesia/harian", 
    function(data){
        const dataset = [];
        const dateset = [];
        for (let i = data.length-7; i < data.length; i++){
            dataset.push(data[i].positif_kumulatif);
            dateset.push(data[i].tanggal);
        }

        const indo_chart = document.getElementById('indo_chart').getContext('2d');

        const new_chart = new Chart(indo_chart, {
            type: 'line',
            data: {
                labels: dateset,
                datasets: [{
                    label: 'positif',
                    data: dataset
                }]
            }
        })
    });

    $("#button_prov").click(function(){
        const inp = $("#input_prov").val();
        $.getJSON("https://apicovid19indonesia-v2.vercel.app/api/indonesia/provinsi", 
        function(data){
            let found = false;
            for (let i in data){
                if (data[i].provinsi.toLowerCase() === inp.toLowerCase()){
                    $('#prov-name').text(data[i].provinsi);
                    $('#jumlah_positif_prov').text(data[i].kasus);
                    $('#jumlah_sembuh_prov').text(data[i].sembuh);
                    $('#jumlah_meninggal_prov').text(data[i].meninggal);
                    found = true;
                    break;
                }
            }
            if (found){
                $("#prov_container").show();
            }
        });
    });
});