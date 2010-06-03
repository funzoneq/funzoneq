
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>22download202</title>
        <link rel="stylesheet" type="text/css" media="screen" href="stylesheets/22download202.css" />
        <script language="JavaScript" src="http://code.jquery.com/jquery-1.4.2.min.js"></script>
        <script language="JavaScript">
            <!--

$(document).ready(function() {
    $('.genre > .info').hide();
    var id = window.location.hash.substr(1);
    if( id )
    {
        $('#'+window.location.hash.substr(1)+' > .info').show();
        window.location.hash = id;
    }
    $('.genre > .name').click(function(e) {
        var info = $('~ .info', this);
        if( info.is(":visible") )
        {
            $('.genre > .info').hide();
            window.location.hash = "";
        }
        else
        {
            $('.genre > .info').hide();
            info.show();
            window.location.hash = this.parentElement.id;
        }
        e.preventDefault();
    }).hover(function(e){
        $(this).addClass("name_hover");
    },function(e){
        $(this).removeClass("name_hover");
    });
});
            //-->
        </script>
    </head>
    <body>

<h1>22downloads</h1>

{content}

    </body>
</html>
