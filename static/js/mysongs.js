$('#playSong').click(function () {
    console.log('hi');
    console.log($(this).attr('name'))
    $('#' + $(this).attr('name')).html('<iframe src="https://embed.spotify.com/?uri=' + $(this).attr('name') + '" width="100%" height="380" frameborder="0" allowtransparency="true"></iframe>')
});
