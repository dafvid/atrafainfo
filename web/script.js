function populate_table(name, data) {
    const tb = document.getElementById(name)
    for (o of data) {
        const r = tb.insertRow(-1)

        itemHTML = ''
        if ('name' in o.buyB){
            itemHTML += o.buyB.count + '&nbsp;<img src="img/'+o.buyB.img+'"/> '+o.buyB.name+' '
        }
        itemHTML += o.buy.count + '&nbsp;<img src="img/'+o.buy.img+'"/> ' +o.buy.name
        r.insertCell(-1).innerHTML = itemHTML
        let sellHTML = '<div>'+o.sell.count + '&nbsp;<img src="img/'+o.sell.img+'"/> '+o.sell.name+'</div>'
        if ('enchantments' in o.sell) {
            for (e of o.sell.enchantments) {
                sellHTML += '<div><small>'+e+'</small></div>'
            }
        }
        r.insertCell(-1).innerHTML = sellHTML
        r.insertCell(-1).innerHTML = o.villager
    }
}

function setup() {
    fetch('data.json')
    .then((r) => r.json())
    .then((d) => {
        document.getElementById('date_span').innerHTML = d.timestamp
        populate_table('sell_body', d.sell);
        populate_table('buy_body', d.buy);

        const vb = document.getElementById('villager_div');
        let tidx = 0;
        for (vk of d.villager_keys) {
            const v = d.villagers[vk]
            vHTML = '<h3>' + v.name + '</h3> lvl ' + v.level + '(' + v.xp + ' exp)</h3>';
            tidx += 1;
            tableId = 'table'+tidx;
            vHTML += '<table><thead><tr><th>Give</th>';
            vHTML += '<th>Get</th></thead><tbody id="'+tableId+'"></tbody></table>';
            vb.innerHTML += vHTML;
            td = document.getElementById(tableId);



            for (o of v.offers) {
                const r = td.insertRow(-1);
                r.insertCell(-1).innerHTML = o.buy.count + '&nbsp;<img src="img/'+o.buy.img+'"/> ' +o.buy.name
                r.insertCell(-1).innerHTML = '<div>'+o.sell.count + '&nbsp;<img src="img/'+o.sell.img+'"/> '+o.sell.name+'</div>'

            }
        }
    })
}

window.onload = setup
