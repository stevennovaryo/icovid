$(document).ready(function(){
    $("#prov_container").hide();

    $.getJSON("https://apicovid19indonesia-v2.vercel.app/api/indonesia", 
    function(data){
        $('#jumlah_positif').text(data.positif.toLocaleString("en-US"));
        $('#jumlah_sembuh').text(data.sembuh.toLocaleString("en-US"));
        $('#jumlah_meninggal').text(data.meninggal.toLocaleString("en-US"));
    });

    $.getJSON("http://apicovid19indonesia-v2.vercel.app/api/indonesia/harian", 
    function(data){
        const dataset_positif = [];
        const dataset_sembuh = [];
        const dataset_meninggal = [];
        const dateset = [];
        for (let i = data.length-30; i < data.length; i++){
            dataset_positif.push(data[i].positif_kumulatif);
            dataset_sembuh.push(data[i].sembuh_kumulatif);
            dataset_meninggal.push(data[i].meninggal_kumulatif);
            dateset.push(data[i].tanggal.split('T')[0]);
        }

        const indo_chart = document.getElementById('indo_chart').getContext('2d');

        const new_chart = new Chart(indo_chart, {
            type: 'line',
            data: {
                labels: dateset,
                datasets: [{
                    label: 'Positif',
                    data: dataset_positif,
                    backgroundColor: 'rgb(255, 188, 188)',
                    borderColor: 'rgb(255, 188, 188)'
                },{
                    label: 'Sembuh',
                    data: dataset_sembuh,
                    backgroundColor: 'rgb(40, 255, 191)',
                    borderColor: 'rgb(40, 255, 191)'
                },{
                    label: 'Meninggal',
                    data: dataset_meninggal,
                    backgroundColor: 'rgb(243, 139, 160)',
                    borderColor: 'rgb(243, 139, 160)'
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
                    $('#jumlah_positif_prov').text(data[i].kasus.toLocaleString("en-US"));
                    $('#jumlah_sembuh_prov').text(data[i].sembuh.toLocaleString("en-US"));
                    $('#jumlah_meninggal_prov').text(data[i].meninggal.toLocaleString("en-US"));
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