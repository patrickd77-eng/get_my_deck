from enum import Enum

# Do not modify. This reflects the position of models on the page, in array style.
# 0 is the first, as 512 OLED is normally at the top of the list. 
# See https://preview.redd.it/refurbished-steam-deck-oled-out-in-the-uk-v0-2aniv7g9s36e1.jpeg?width=640&crop=smart&auto=webp&s=66b3a91fa53cf1f086736ccef81e4041c80ae9db 
# for an example of recent ordering.
class SteamDeckModel(Enum):
    OLED_512GB = 0
    OLED_1TB = 1
    LCD_64GB = 2
    LCD_256GB = 3
    LCD_512GB = 4

# HTML example of the Steam Deck models from Jan 2025
# <div class="_1cOoCFwafBlSkwllIMf3XM _39HWXhhjsbML7K9sme9ItV SaleSectionForCustomCSS" style="padding-left: 0px; padding-right: 0px;">
#    <div class="bE2EA4JB9SDa1PZ7HSFL-"></div>
#    <div class="Panel Focusable">
#       <div class="_3gb3JeV_1IMaIeODzBSrP3 W9_WAYXgEe-t-7aqqC4Jp center_row_trgt ItemCount_1">
#          <div class="capsule_index_0">
#             <div class="ImpressionTrackedElement">
#                <div class="Panel Focusable">
#                   <div class="VvwZmAlF0uXfe__ZO0uX0">
#                      <div class="_1e4No10_bpJEyqWGdzhAs9">Steam Deck 512 GB OLED - Valve Certified Refurbished</div>
#                      <div>
#                         <div class="kW6m4Sjqacp5hykrj5LEo m8h0cksva38onSt9vDraW">
#                            <div class="_1JuIpzMtS7-xZrnUmEQ4my">
#                               <div class="_3XwnF5hpyOwvxFT_v7PMhS CartBtn"><span> Out of stock</span></div>
#                               <div class="_2s-O5T3qJJYR2AUq4b9jIN StoreSalePriceWidgetContainer">
#                                  <div class="_3j4dI1yA7cRfCvK8h406OB">£389.00</div>
#                               </div>
#                            </div>
#                         </div>
#                      </div>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#       <div class="_3gb3JeV_1IMaIeODzBSrP3 W9_WAYXgEe-t-7aqqC4Jp center_row_trgt ItemCount_1">
#          <div class="">
#             <div class="ImpressionTrackedElement">
#                <div class="Panel Focusable">
#                   <div class="VvwZmAlF0uXfe__ZO0uX0">
#                      <div class="_1e4No10_bpJEyqWGdzhAs9">Steam Deck 1TB OLED - Valve Certified Refurbished</div>
#                      <div>
#                         <div class="kW6m4Sjqacp5hykrj5LEo m8h0cksva38onSt9vDraW">
#                            <div class="_1JuIpzMtS7-xZrnUmEQ4my">
#                               <div class="_3XwnF5hpyOwvxFT_v7PMhS CartBtn"><span> Out of stock</span></div>
#                               <div class="_2s-O5T3qJJYR2AUq4b9jIN StoreSalePriceWidgetContainer">
#                                  <div class="_3j4dI1yA7cRfCvK8h406OB">£459.00</div>
#                               </div>
#                            </div>
#                         </div>
#                      </div>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#       <div class="_3gb3JeV_1IMaIeODzBSrP3 W9_WAYXgEe-t-7aqqC4Jp center_row_trgt ItemCount_1">
#          <div class="">
#             <div class="ImpressionTrackedElement">
#                <div class="Panel Focusable">
#                   <div class="VvwZmAlF0uXfe__ZO0uX0">
#                      <div class="_1e4No10_bpJEyqWGdzhAs9">Steam Deck 64 GB LCD - Valve Certified Refurbished</div>
#                      <div>
#                         <div class="kW6m4Sjqacp5hykrj5LEo m8h0cksva38onSt9vDraW">
#                            <div class="_1JuIpzMtS7-xZrnUmEQ4my">
#                               <div class="_3XwnF5hpyOwvxFT_v7PMhS CartBtn"><span> Out of stock</span></div>
#                               <div class="_2s-O5T3qJJYR2AUq4b9jIN StoreSalePriceWidgetContainer">
#                                  <div class="_3j4dI1yA7cRfCvK8h406OB">£249.00</div>
#                               </div>
#                            </div>
#                         </div>
#                      </div>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#       <div class="_3gb3JeV_1IMaIeODzBSrP3 W9_WAYXgEe-t-7aqqC4Jp center_row_trgt ItemCount_1">
#          <div class="">
#             <div class="ImpressionTrackedElement">
#                <div class="Panel Focusable">
#                   <div class="VvwZmAlF0uXfe__ZO0uX0">
#                      <div class="_1e4No10_bpJEyqWGdzhAs9">Steam Deck 256 GB LCD - Valve Certified Refurbished</div>
#                      <div>
#                         <div class="kW6m4Sjqacp5hykrj5LEo m8h0cksva38onSt9vDraW">
#                            <div class="_1JuIpzMtS7-xZrnUmEQ4my">
#                               <div class="_3XwnF5hpyOwvxFT_v7PMhS CartBtn"><span> Out of stock</span></div>
#                               <div class="_2s-O5T3qJJYR2AUq4b9jIN StoreSalePriceWidgetContainer">
#                                  <div class="_3j4dI1yA7cRfCvK8h406OB">£279.00</div>
#                               </div>
#                            </div>
#                         </div>
#                      </div>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#       <div class="_3gb3JeV_1IMaIeODzBSrP3 W9_WAYXgEe-t-7aqqC4Jp center_row_trgt ItemCount_1">
#          <div class="">
#             <div class="ImpressionTrackedElement">
#                <div class="Panel Focusable">
#                   <div class="VvwZmAlF0uXfe__ZO0uX0">
#                      <div class="_1e4No10_bpJEyqWGdzhAs9">Steam Deck 512 GB LCD - Valve Certified Refurbished</div>
#                      <div>
#                         <div class="kW6m4Sjqacp5hykrj5LEo m8h0cksva38onSt9vDraW">
#                            <div class="_1JuIpzMtS7-xZrnUmEQ4my">
#                               <div class="_3XwnF5hpyOwvxFT_v7PMhS CartBtn"><span> Out of stock</span></div>
#                               <div class="_2s-O5T3qJJYR2AUq4b9jIN StoreSalePriceWidgetContainer">
#                                  <div class="_3j4dI1yA7cRfCvK8h406OB">£319.00</div>
#                               </div>
#                            </div>
#                         </div>
#                      </div>
#                   </div>
#                </div>
#             </div>
#          </div>
#       </div>
#    </div>
# </div>