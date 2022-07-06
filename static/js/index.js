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

function get ( url, method, callback ) {
    var req = new XMLHttpRequest();
    req.open( method.toUpperCase(), url );
    req.send();
    req.onreadystatechange = function () {
        setTimeout( function () {
            callback( req );
        }, 200 );
    };
};
