function showTextcaption(id) {
    id.innerHTML="D'origine latine, « alias » signifie « une autre fois », « autrement »";

}

function showTextadip(id) {
    id.innerHTML="L'adresse ip est notre adresse sur internet";

}
function showTextport(id) {
    id.innerHTML="Le port permet de faire appel à des services différents";
    
}
function showTextalias(id) {
    id.innerHTML="L'Alias est blblalbalbalba";
    
}

function updateAlias() {
    $.getJSON('/alias_JSON', function(alias_JSON) {
        console.log(alias_JSON)
    });
  }

setInterval(updateAlias, 60000);