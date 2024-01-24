sn = '''AL
AK
AA
AE
AP
AS
AZ
AR
CA
CO
CT
DE
DC
FM
FL
GA
GU
HI
ID
IL
IN
IA
KS
KY
LA
MH
MA
ME
MD
MS
MI
MN
MO
MT
NE
NV
NH
NJ
NM
NY
NC
ND
MP
OH
OK
OR
PW
PA
PR
RI
SC
SD
TN
TX
UT
VT
VA
VI
WA
WV
WI
WY'''

ft = '''(any state)
AL - Alabama                       
AK - Alaska                        
AA - American Atlantic (APO/FPO)   
AE - American Europe (APO/FPO)     
AP - American Pacific (APO/FPO)    
AS - American Samoa                
AZ - Arizona                       
AR - Arkansas                      
CA - California                    
CO - Colorado                      
CT - Connecticut                   
DE - Delaware                      
DC - District of Columbia          
FM - Federated States of Micronesia
FL - Florida                       
GA - Georgia                       
GU - Guam                          
HI - Hawaii                        
ID - Idaho                         
IL - Illinois                      
IN - Indiana                       
IA - Iowa                          
KS - Kansas                        
KY - Kentucky                      
LA - Louisiana                     
MH - Marshall Islands              
MA - Massachusetts                 
ME - Maine                         
MD - Maryland                      
MS - Mississippi                   
MI - Michigan                      
MN - Minnesota                     
MO - Missouri                      
MT - Montana                       
NE - Nebraska                      
NV - Nevada                        
NH - New Hampshire                 
NJ - New Jersey                    
NM - New Mexico                    
NY - New York                      
NC - North Carolina                
ND - North Dakota                  
MP - Northern Mariana Islands      
OH - Ohio                          
OK - Oklahoma                      
OR - Oregon                        
PW - Palau                         
PA - Pennsylvania                  
PR - Puerto Rico                   
RI - Rhode Island                  
SC - South Carolina                
SD - South Dakota                  
TN - Tennessee                     
TX - Texas                         
UT - Utah                          
VT - Vermont                       
VA - Virginia                      
VI - Virgin Islands                
WA - Washington                    
WV - West Virginia                 
WI - Wisconsin                     
WY - Wyoming                '''










sn = sn.split('\n')
ft = ft.split('\n')

dict(zip(sn,[i.strip() for i in ft[1:]]))


# states_names = []
# for i in range(len(sn)):
#     sn_item = sn[i]
#     ft_item = ft[i].strip()

#     new_item = {sn_item:ft_item}
#     states_names.append(new_item)

# states_names
