function showLog() {
  $(document).ready(function() {
    $.ajax({
        async:false,
        url: 'icovid/log/web_log.log',
        dataType: 'text',
        success: function(data) 
        {
        $('#web-log').append(data);
            }
        });
    });
};
