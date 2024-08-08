/** @odoo-module **/

import TicketScreen from 'point_of_sale.TicketScreen';
import Registries from 'point_of_sale.Registries'; 
const { useState} = owl;

export const TicketScreenBits = (TicketScreen) =>
    class extends TicketScreen {
        setup() {
            super.setup();  
            this.isNumpad_shown = true; 
            this.isNumpad_shown =  useState({'isNumpad_shown': true});  
        }
        ToggleNumpad(ev){ 
            $(ev.target).parents('.leftpane').find('.pads').toggleClass('hidden');
            if(this.isNumpad_shown.isNumpad_shown){
                this.isNumpad_shown.isNumpad_shown = false ;
            }else{
                this.isNumpad_shown.isNumpad_shown = true ;
            }
        }
    }
Registries.Component.extend(TicketScreen, TicketScreenBits);  