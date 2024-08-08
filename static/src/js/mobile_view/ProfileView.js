/** @odoo-module **/

const PosComponent = require('point_of_sale.PosComponent');
const Registries = require('point_of_sale.Registries'); 
const { useListener } = require("@web/core/utils/hooks");

class ProfileView extends PosComponent { 
    setup() {
        super.setup();
        useListener('close-screen', this._onCloseScreen);
        this.showLabel = true;
    }
    _onCloseScreen() { 
        if(this.env.pos.config.iface_floorplan){
            this.showScreen('FloorScreen');
        }else{
            this.showScreen('ProductScreen');
        }
        
    } 
    get username() {
        const { name } = this.env.pos.get_cashier();
        return name ? name : '';
    }
    get avatar() {
        const user_id = this.env.pos.get_cashier_user_id();
        const id = user_id ? user_id : -1;
        return `/web/image/res.users/${id}/avatar_128`;
    }
}
 ProfileView.template = 'ProfileView';

Registries.Component.add( ProfileView);

return  ProfileView; 