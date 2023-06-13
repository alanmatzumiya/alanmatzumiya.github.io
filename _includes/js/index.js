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
  
function fprint ( y ) {

    var ystring = "";
    if ( ["array", "object"].includes(datatype( y )) ) {
        ystring += JSON.stringify( y );
    } else {
        ystring += y;
    };
    console.log( ystring );

};

