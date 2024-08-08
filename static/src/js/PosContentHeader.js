/** @odoo-module **/

const PosComponent = require('point_of_sale.PosComponent');
const Registries = require('point_of_sale.Registries'); 

class PosContentHeader extends PosComponent {
    setup(){
        const date = new Date();
        this.meridiem = date.getHours() < 12 ? 'Morning' : 'Evening';
    }
    ToggleMenu(ev){ 
        $(ev.target).parents('.pos').find('.pos-topheader').toggleClass('lb_visible')
    }
}
PosContentHeader.template = 'PosContentHeader';

Registries.Component.add(PosContentHeader);

return PosContentHeader; 