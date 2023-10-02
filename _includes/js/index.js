function datatype ( value ) {

    if ( value === null ) {
        return "null";
    }

    const baseType = typeof value

    if (!["object", "function"].includes( baseType )) {
        return baseType.toLowerCase();
    }

    const tag = value[Symbol.toStringTag];

    if ( typeof tag === "string" ) {
        return tag.toLowerCase();
    }

    if (
        baseType === "function" &&
        Function.prototype.toString.call(value).startsWith("class")
    ) {
        return "class";
    }

    const className = value.constructor.name;

    if ( typeof className === "string" && className !== "" ) {
        return className.toLowerCase();
    }

    return baseType.toLowerCase();

};

function callable ( func ) {
    return type( func ) == "function";
};

function isdefined ( x ) {
    return x != undefined;
};

function fprint ( y ) {

    var ystring = "";
    if ( ["array", "object"].includes(datatype( y )) ) {
        ystring += JSON.stringify( y );
    } else if ( datatype( y ) == "htmlbuttonelement" ) {
        ystring += y.outerHTML;
    } else {
        ystring += y;
    };
    console.log( ystring );

};

function getkeys ( x ) {
    return Object.keys( x );
};
function getvalues ( x ) {
    return Object.values( x );
};
function getitems ( x ) {
    return Object.entries( x );
};

function urlData () {
    var data = {
        url: location.href,
        path: location.pathname,
        port: location.port,
        protocol: location.protocol.split(":")[0],
        host: location.hostname
    };
    return data;
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