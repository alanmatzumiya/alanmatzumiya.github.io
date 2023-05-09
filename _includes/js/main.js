function print ( y ) {
    console.log(
        ( typeof(y) == "object" ) ? JSON.stringify( y ) : y
    );
};

function isdefined ( x ) {
    return x != undefined;
};

function type ( x ) {
    var xtype = typeof( x );
    if ( xtype == "object" ) {
        return (
            isdefined( x.length )
        ) ? "array" : xtype;
    } else {
        return xtype;
    };
};

function callable ( func ) {
    return type( func ) == "function";
};

function urlparse ( url, params ) {
    return url + "?" + Object.entries( params ).map(
        x => x[0] + "=" + x[1]
    ).join("&");
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

function redirectTo ( url ) {
    window.location.href = url;
};

function round ( x ) {
    return Math.round( x );
};

function winSize () {

    var xy = {
        w_val: function ( scale=1.0 ) {
            return round( window.innerWidth ) * scale;
        },
        h_val: function ( scale=1.0 ) {
            return round( window.innerHeight ) * scale;
        },
        w: function ( scale=1.0 ) {
            return this.w_val( scale ) + "px";
        },
        h: function( scale=1.0 ) {
            return this.h_val( scale ) + "px";
        }
    };

    return xy;

};

function show( e ) {
  e.style.display = "block";
};

function hide( e ) {
  e.style.display = "none";
};


/*
--------------------------------------------------------------------------------------------------------------
    Sub-Module: Http-Methods
--------------------------------------------------------------------------------------------------------------
*/


function Http ( url="/" ) {

    var xhttp = {
        url: ( url == "/" ) ? document.URL.slice(0, -1) : url,
        fprint: print,
        data: {},
        timeout: 5e2
    };

    xhttp.urlparse = function ( params ) {
         return this.url + "?" + getitems( params ).map(
            x => x[0] + "=" + x[1]
         ).join("&");
    };

    xhttp.getjson = function ( path, func ) {
        var xurl = [this.url, path].join("/");
        var req = this.data;
        var fprint = this.fprint;
        var tout = this.timeout;
        $.getJSON(
            xurl, req, function( data ) {
               setTimeout( function () {
                    fprint( data );
                    if ( callable( func ) ) {
                        func( data );
                    };
               }, tout );
            }
        );
    };

    return xhttp;

};

function getsize ( e ) {
    var size = e.getBoundingClientRect();
    return {
        w: size.width,
        h: size.height,
        x: size.x,
        y: size.y
    };
};

function getpos ( e ) {
    var p = e.getBoundingClientRect();
    return {
        x: [p.left, p.right],
        y: [p.bottom, p.top],
        w: p.width,
        h: p.height
    };
};

function copy ( e ) {
    return e.cloneNode(true);
};

function getnodes ( e, cls ) {
    return getvalues( e.querySelectorAll( cls ) );
};

function getchild ( e, cls ) {
    return getvalues( e.querySelector( cls ).childNodes );
};

function setsize ( e, name, value ) {

    var efunc = {
        x: function () {
            var dx = getpos( e ).w;
            e.style.left = value + "px";
            e.style.width = dx + "px";
        },
        y: function () {
            var dy = getpos( e ).h;
            e.style.bottom = value + "px";
            e.style.height = dy + "px";
        },
        w: function () {
            e.style.width = value + "px";
        },
        h: function () {
            e.style.height = value + "px";
        }
    };
    efunc[ name ]();

};

function tquery ( q, v, first=true ) {

    function setter ( e ) {
        e.getsize = function () {
            return getsize( e );
        };
        e.pos = function () {
            return getpos( e );
        };
        e.hide = function () {
            hide( e );
        };
        e.show = function () {
            show( e );
        };
        e.copy = function () {
            return copy( e );
        };
        e.nodes = function ( cls ) {
            return getnodes( e, cls );
        };
        e.child = function ( cls ) {
            return getchild( e, cls );
        };
        e.setX = function ( value ) {
            setsize( e, "x", value );
        };
        e.setY = function ( value ) {
            setsize( e, "y", value );
        };
        e.setW = function ( value ) {
            setsize( e, "w", value );
        };
        e.setH = function ( value ) {
            setsize( e, "h", value );
        };
    };

    if ( q == "id" ) {
        var e = $( "#" + v )[0];
        setter( e );
        return e;
    } else if ( q == "class" || q == "tag" ) {
        var e = $( ( q == "class" ) ? "." + v : v );
        if ( first ) {
            e = e[0];
            setter( e );
            return e;
        } else {
            for ( x of getitems( e ) ) {
                var ei = x[1];
                setter( ei );
                e[x[0]] = ei;
            };
            return e;
        };
    };

};


function newElement ( name, content ) {

    var e = document.createElement( name );
    e.innerHTML = content;
    return e;

};
