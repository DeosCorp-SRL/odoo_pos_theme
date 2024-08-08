/** @odoo-module **/

const PosComponent = require('point_of_sale.PosComponent');
const Registries = require('point_of_sale.Registries'); 
const { useListener } = require("@web/core/utils/hooks");

class BottomMenus extends PosComponent { 
    setup() {   
        super.setup();
        useListener('open-menus',this.OpenMenus) 
    }
    async OpenMenus(ev){
        $(ev.target).parents('.pos').find('.pos-topheader').toggleClass('lb_visible')
    }
    get order() {
        return this.env.pos.get_order();
    }
    get total() {
        const _total = this.order ? this.order.get_total_with_tax() : 0;
        return this.env.pos.format_currency(_total);
    }
    get total_without_curr() {
        const _total = this.order ? this.order.get_total_with_tax() : 0;
        return _total;
    }
    get items_number() {
        return this.order ? this.order.orderlines.reduce((items_number,line) => items_number + line.quantity, 0) : 0;
    }
    get count() {
        if (this.env.pos) {
            return this.env.pos.get_order_list().length;
        } else {
            return 0;
        }
    }
    onClick() {
        if (this.props.isTicketScreenShown) {
            this.env.posbus.trigger('ticket-button-clicked');
        } else {
            this.showScreen('TicketScreen');
        }
    }  
}
BottomMenus.template = 'BottomMenus';

Registries.Component.add(BottomMenus);

return BottomMenus; 