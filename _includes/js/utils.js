/*
==================================================
    Module: Utils
==================================================
*/

/*
--------------------------------------------------------------------------------------------------------------
    Sub-Module: Object
--------------------------------------------------------------------------------------------------------------
*/

function isdefined ( x ) {
    return x != undefined;
}

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

function print ( x ) {
    console.log(
        ( type( x ) == "object" ) ? JSON.stringify( x ) : x
    );
};

function round ( x ) {
    return Math.round( x );
};

function abs ( x ) {
    return Math.abs( x );
};

function random ( a, b ) {
    var r = Math.random();
    if ( a != undefined && b != undefined ) {
        return a + round( r * abs( b - a ) )
    } else {
        return r;
    };
};

function sample ( data, size ) {
    var xn;
    size = ( size > data.length  ) ? data.length : size;
    var xdata = [data[ random( 0, data.length - 1 ) ]];
    while ( xdata.length < size ) {
        xn = data[ random( 0, data.length - 1 ) ];
        if ( xdata.indexOf( xn ) == -1 ) {
            xdata.push( xn );
        };
    };
    return xdata;
};

function Precision ( x , n ) {
  	var xn = Math.trunc( x );
  	var yn = Math.trunc( ( x - xn ) * 10 ** n );
    return parseFloat( xn + "." + yn );
};

function range ( a, b, dx=1 ) {
    if ( b == undefined ) {
        b = a; a = 0;
    };
    return Array.from(
        {length: (b - a - 1) / dx + 1}, ( _, i ) => a + ( i * dx )
    );
};

function grid ( a, b, n ) {
    var dx = (b - a) / n;
    return range(0, n + 1).map( i => a + i * dx );
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

function merge ( x, y ) {
    var xy;
    if ( type( x ) == "object" && type( y ) == "object" ) {
        xy = { ...x, ...y };
    } else if ( type( x ) == "array" && type( y ) == "array" ) {
        xy = [ ...x, ...y ].sort();
    };
    return xy;
};

function show( e ) {
  e.style.display = "block";
};

function hide( e ) {
  e.style.display = "none";
};


function bodySize ( scale=1.0 ) {
    var y = document.body;
    return {
        w: round( y.clientWidth * scale ) + "px",
        h: round( y.clientHeight * scale ) + "px"
    };
};


function getElement ( q, v, first=true ) {
    if ( q == "id" ) {
        var e = $( "#" + v )[0];
        setElement( e );
        return e;
    } else if ( q == "class" || q == "tag" ) {
        var e = $( ( q == "class" ) ? "." + v : v );
        if ( first ) {
            e = e[0];
            setElement( e );
            return e;
        } else {
            for ( x of getitems( e ) ) {
                var ei = x[1];
                setElement( ei );
                e[x[0]] = ei;
            };
            return e;
        };
    };
};

function createElement ( name, content="" ) {
    var e = document.createElement( name );
    e.innerHTML = content;
    return e;
};

function setElement ( e ) {

    e.getsize = function () {
        var size = this.getBoundingClientRect();
        return {
            w: size.width,
            h: size.height,
            x: size.x,
            y: size.y
        };
    };

    e.pos = function () {
        var pos = this.getBoundingClientRect();
        return {
            x: [pos.left, pos.right],
            y: [pos.bottom, pos.top],
            w: pos.width,
            h: pos.height
        };
    };

    e.setX = function ( x ) {
        var dx = this.pos().w;
        this.style.left = x + "px";
        this.style.width = dx + "px";
    };
    e.setY = function ( y ) {
        var dy = this.pos().h;
        this.style.bottom = y + "px";
        this.style.height = dy + "px";
    };
    e.setW = function ( w ) {
        this.style.width = w + "px";
    };
    e.setH = function ( h ) {
        this.style.height = h + "px";
    };

    e.hide = function () {
        this.style.display = "none";
    };
    e.show = function () {
        this.style.display = "block";
    };

    e.copy = function () {
        return this.cloneNode(true);
    };

    e.queryNodes = function ( cls, func ) {
        return getvalues( this.querySelector( cls ).childNodes );
    };
    e.query = function ( cls ) {
        return getvalues( this.querySelectorAll( cls ) );
    };

};


function getDate () {
    var tdata = new Date();
    var date = {};
    date.full = tdata.toLocaleTimeString();
    var keyvalues = [
        ["Hours","hr"],
        ["Minutes", "min"],
        ["Seconds", "sec"]
    ];
    for ( x of keyvalues ) {
        date[ x[1] ] = tdata[ "get" + x[0] ]();
    };
    return date;
};


function openwindow ( url ) {

    return window.open(
        url, "_blank",
        Object.entries( {
            toolbar: "yes",
            scrollbars: "yes",
            resizable: "yes",
            top: 500,
            left: 500,
            width: 400,
            height: 400
        } ).map(
            v => `${v[0]}=${v[1]}`
        ).join( "," )
    );

};

function fadeEvent ( id ) {

    $( "#" + id ).click( function () {
        $("#div1").fadeIn();
        $("#div2").fadeIn("slow");
        $("#div3").fadeIn(3000);
    } );

};


function createBrowser () {

    var browser = {};

    browser.page = {
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "facebook": "https://www.facebook.com"
    };

    browser.open = function( url ) {
        window.location = url;
    };

    browser.loadPage = function () {
        window.scrollTo( 0, this.scrollMaxY );
    };

    return browser;

};

class ClassObject {
    constructor(name) {
        this.name = name;
        this.data = {};
    }
    Data() {
        console.log(this.nombre + ' starting');
    }
};

class createObject extends ClassObject {
    Data() {
        super.Data();
        console.log(this.nombre + ' finish');
    }
};

/*
--------------------------------------------------------------------------------------------------------------
    Sub-Module: Http-Methods
--------------------------------------------------------------------------------------------------------------
*/

function joinpath(url={ root: "", path: "", pathlist: [] }) {
    if ( url.root.endsWith("/") ) {
        url.root = url.root.slice(0, -1)
    };
    if ( type(url.path) == "string" ) {
        if ( url.path.startsWith("/") ) {
            url.path = url.path.slice(1)
        };
        return [url.root, url.path].join("/");
    } else if ( type(url.pathlist) == "array" ) {
        return [url.root].concat(url.pathlist).join("/");
    };
};

function redirectTo ( url ) {
    window.location.href = url;
};


function Http ( url="/" ) {

    var obj = {
        url: url,
        seturl: function ( path ) {
            if ( isdefined( path ) ) {
                return [
                    url, path[0].replace( "/", "" ) + path.slice(1)
                ].join( "/" );
            } else {
                return url;
            };
        }
    };

    obj.urlparse = function ( path, data ) {
        if ( type( data ) == "object" ) {
            return path + "?" + getitems(data).map(
                x => `${x[0]}=${x[1]}`
            ).join( "&" );
        } else {
            return path;
        };
    };

    obj.getjson = function ( path, handler=print, req={} ) {
        $.getJSON(
            this.seturl( path ), req,
            ( data ) => setTimeout(
                () => handler( data ), 5e2
            )
        );
    };

    obj.get = function ( path, handler=print ) {
        var req = new XMLHttpRequest();
        req.open( "GET", this.seturl( path ) );
        req.send();
        req.onreadystatechange = function () {
            setTimeout( function () {
                handler( req.responseText );
            }, 5e2 );
        };
    };

    obj.post = function ( path, req, handler=print ) {
        print( this.seturl( path ) );
        $.post(
            this.seturl( path ), req,
            ( data ) => setTimeout(
                () => handler( data ), 5e2
            )
        );
    };

    return obj;
};

function AsyncProcess ( func, data ) {

    function Resolve () {
      return new Promise(
        result => {
          setTimeout( () => { result( func(data) ) }, 1e3 )
        }
      );
    };

    async function Exec () {
      const result = await Resolve();
      console.log(result);
    };

    return Exec;

  };






  // Import Modules

{% include module/utils.js %}

{% include module/plot.js %}

/*
==================================================
    BUILTINS
==================================================
*/

{% assign app = site.data.app %}

var app = Http( '{{ site.app }}' );

app.env = function () {
    return '{{ jekyll.environment }}';
};

function fromStatic ( path ) {
    return Http( ['{{ site.static_url }}', path].join("/") );
};

function createLogin ( id, btn_id ) {
	var login = getElement( "id", id );
	getElement( "id", btn_id ).onclick = function() {
    	getElement( "class", "menu-close" ).click();
    	login.show();
	};
	login.query( "span.close" ).map(
		ei => ei.onclick = function () { login.hide() }
	);
	window.onclick = function( event ) {
		if ( event.target == login ) {
			login.hide();
		};
	};
};

function getLogIn () {

    var login = $( "#login-data" )[0];
    login.get = login.querySelector( ".login-button" );
    login.get.onclick = function () {
        print({
            username: login.querySelector( "input[name=username]" ).value,
            password: login.querySelector( "input[name=password]" ).value
        });
    };

};

function getJupyter ( topic ) {

    function getDropDown ( id, content ) {

        var Header = content.header;
        var Body = content.body;
        return `{%
            include {{ site.module-element.accordion }}
            id='${id}' header='${Header}' body='${Body}'
        %}`;

    };

    function handler ( x ) {

        var content = x.content;
        var outdata = "";
        var tbody = "";

        for ( m of getkeys( content[topic] ) ) {
            var mbody = "<ul>";
            for ( xi of content[topic][m] ) {
                mbody += '<li><a href="' + [x.root, xi.path].join("/") + '">' + xi.name.replace(".ipynb", "") + '</a></li>';
            };
            mbody +=  "</ul>";
            tbody += getDropDown(
                topic + "_" + m,
                { header: "Module " + m, body: mbody }
            );
        };
        outdata += getDropDown(
            topic,
            {
                header: topic.split( "_" ).map(
                    ti => ti[0].toUpperCase() + ti.slice(1)
                ).join( " " ),
                body: tbody
            }
        );

        $( "#jupyter-" + topic )[0].innerHTML = outdata;

    };

    fromStatic( "data" ).getjson(
        "notebooks.json", handler
    );

};


/*
==================================================
    Builtins
==================================================
*/
function Timer() {
    return {
        counter: {
            value: 0,
            next: function () { this.value += 1 },
            back: function () { this.value -= 1 },
            reset: function () { this.value = 0 }
        },
        init: function ( n, delay=1e3, new_counter=true ) {
            var log = console.log;
            var counter = this.counter;
            if ( new_counter ) {
                counter.reset();
            };
            log( "starting to count" )
            var interval = setInterval( function () {
                if ( counter.value < n ) {
                    counter.next();
                    log( "i="+counter.value );
                } else {
                    clearInterval( interval );
                    log( "count terminated" );
                };
            }, delay );
        },
        sleep: function ( t ) {
            var log = console.log;
            log( "start sleeping..." );
            this.init( t );
            setTimeout( function () { log( "wake up !!!" ) }, ( t + 1 ) * 1e3 );
        },
        clock: function () {
            var t = new Date();
            var tdata = {};
            tdata.full = t.toLocaleTimeString();
            [ ["Hours","hr"], ["Minutes", "min"], ["Seconds", "sec"] ].map(
                s => tdata[ s[1] ] = t[ "get" + s[0] ]()
            );
            return tdata;
        },
        date: function () {
            var d = new Date();
            return d.toLocaleDateString();
        }
    };
};


function createConsole () {
    var x = $( "#console" )[0];

    x.innerHTML = [
        '<div class="console-out" ></div>',
        '<input class="console-in" type="text" />',
        '<button class="console-run" > Run </button>'
    ].join( "\n" );

    var input = x.querySelector( ".console-in" );
    var output = x.querySelector( ".console-out" );

    x.querySelector( ".console-run" ).onclick = function () {
        output.innerHTML = eval( input.value );
    };

};


function saveFile ( name, data ) {
    data = JSON.stringify( data, null, 4 );
    if ( typeof( Blob ) != "undefined" ) {
        var textFileAsBlob = new Blob(
            [data],
            {type: 'text/plain'}
        );
        var downloadLink = document.createElement("a");
        downloadLink.download = name;
        if ( window.webkitURL != null ) {
            downloadLink.href = window.webkitURL.createObjectURL(textFileAsBlob);
        } else {
            downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
            downloadLink.onclick = document.body.removeChild(event.target);
            downloadLink.style.display = "none";
            document.body.appendChild(downloadLink);
        }
        downloadLink.click();
    } else {
        var pp = document.createElement('a');
        pp.setAttribute(
            'href',
            'data:text/plain;charset=utf-8,' + encodeURIComponent( data )
        );
        pp.setAttribute('download', name);
        pp.onclick = document.body.removeChild(event.target);
        pp.click();
    };
};

function getTemplate ( id, content_id ) {

    var template = $( "#" + id )[0];
    var content = $( "#" + content_id )[0];
    cloned = template.content.cloneNode( true );
    content.textContent = cloned.textContent;

};


function initSocket () {

    function message ( name ) {
        return print({
            starting: "starting to count",
            sleeping: "start sleeping...",
            terminated: "count terminated"
        }[name]);
    };

    var socket = {
        kill: function ( id ) {
            if ( this.register[id] != undefined  ) {
                delete this.register[id];
            };
        },
        register: {}
    };

    socket.create = function ( id ) {

        var sock = {};

        sock.id = id;
        sock.connected = false;

        sock.data = {};
        sock.task = null;
        sock.connect = function () {
            this.connected = true;
        };
        sock.disconnect = function () {
            this.connected = false;
        };

        counter = {};
        counter.value = 0;
        counter.next = function () {
            this.value += 1;
        };
        counter.back = function () {
            this.value -= 1;
        };
        counter.reset = function () {
            this.value = 0;
        };
        sock.counter = counter;

        sock.do_task = function ( func, secs, delay=1 ) {
            sock.counter.reset();
            message( "starting" );
            sock.task = setInterval( function () {
                if ( sock.counter.value < secs ) {
                    sock.counter.next();
                    print( "i="+sock.counter.value );
                    func();
                } else {
                    clearInterval( sock.task );
                    message( "terminated" );
                };
            }, delay * 1e3 );

        };

        sock.sleep = function ( t ) {
            message( "starting" );
            setTimeout(
                function () {
                    print( "wake up !!!" );
                },
            t * 1e3 );
        };

        socket.register[id] = sock;

    };

    return socket;

};


/*
==================================================
    Site-Data
==================================================
*/


var currentPage = '{{ page.title }}';
var sitePages = [];

{%- for p in site.pages -%}
{%- if p.title -%}
sitePages.push({
    "title": '{{ p.title }}',
    "name": '{{ p.name }}',
    "image": '{{ p.image }}',
    "url": '{{ p.url }}',
    "path": '{{ p.path }}',
    "tags": {{ p.tags | split: ", " | jsonify }}
});
{%- endif -%}
{%- endfor -%}