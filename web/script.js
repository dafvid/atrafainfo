function populate_table(name, data) {
    const tb = document.getElementById(name)
    for (o of data) {
        const r = tb.insertRow(-1)

        if ('name' in o.buyB){
            r.insertCell(-1).innerHTML = o.buyB.count + ' ' +o.buyB.name
        } else {
            r.insertCell(-1).innerHTML = ''
        }
        r.insertCell(-1).innerHTML = o.buy.count + '&nbsp;' +o.buy.name
        let sellHTML = '<div>'+o.sell.count + '&nbsp;' +o.sell.name+'</div>'
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
        console.log(d.offers);
        document.getElementById('date_span').innerHTML = d.timestamp
        populate_table('sell_body', d.sell);
        populate_table('buy_body', d.buy);

        const vb = document.getElementById('villager_body')
        for (vk of d.villager_keys) {
            const v = d.villagers[vk]
            const r = vb.insertRow(-1)
            r.insertCell(-1).innerHTML = v.name
            r.insertCell(-1).innerHTML = v.level
            r.insertCell(-1).innerHTML = v.xp

        }
    })
}

window.onload = setup
