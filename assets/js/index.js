function print ( y ) {
    console.log(
        ( typeof(y) == "object" ) ? JSON.stringify( y ) : y
    );
};

function urlparse ( url, params ) {
    return url + "?" + Object.entries( params ).map(
        x => x[0] + "=" + x[1]
    ).join("&");        
};

function get ( url ) {
    var req = new XMLHttpRequest();
    req.open( "GET", url );
    req.send();
    req.onreadystatechange = function () {
        setTimeout( function () {
            print( req );
        }, 5e2 );
    };
};
