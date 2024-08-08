/** @odoo-module **/

import ProductScreen from 'point_of_sale.ProductScreen';
import Registries from 'point_of_sale.Registries'; 
const { useState} = owl;

export const ProductScreenBits = (ProductScreen) =>
    class extends ProductScreen {   
        setup() {
            super.setup();   
            this.numpad_is_shown =  useState({'numpad_is_shown': true});  
        }
        ToggleNumpad(ev){  
            $(ev.target).parents('.leftpane').find('.pads').toggleClass('hidden');
            if(this.numpad_is_shown.numpad_is_shown){
                this.numpad_is_shown.numpad_is_shown = false ;
            }else{
                this.numpad_is_shown.numpad_is_shown = true ;
            }
        }
        ToggleMenu(ev) {
            var link_btns = $(ev.currentTarget).parents('.pos-topheader').find('.link-btn-text') 
            link_btns.toggleClass('hide');
            $(ev.currentTarget).parents('.oe_sidebar').toggleClass('lb_visible') 
        }
        switchTab(ev){
            let currentTarget = $(ev.currentTarget);
            let id = currentTarget.getAttributes().id ? currentTarget.getAttributes().id : false; 
            currentTarget.parent().find('.active').removeClass('active');
            currentTarget.parent().find('#'+id).addClass('active');
            
            let tabsContainer = currentTarget.parents('.leftpane').find('.custom-tabs-content');
            tabsContainer.find('.tab-content.active').removeClass('active');
            tabsContainer.find('#'+id).addClass('active');
        } 
    };  

Registries.Component.extend(ProductScreen, ProductScreenBits);  
