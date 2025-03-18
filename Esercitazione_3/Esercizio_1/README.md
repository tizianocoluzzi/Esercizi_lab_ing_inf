# Esercizio 1
## esempio di e-store
esercizio per sviluppare una rest api sull'esempio di e-store, parto dalla commit dell'esrcizio 1 dell'eserciazione 2 del 18.03 alle 10:00, potrebbe differenziarsi di molto
## API
* GET get_inventory: restituiusce l'inventario dello store
* GET get_user_items: oggetti posseduto dall'utente
* GET get_item_information; informazioni di un item 
* GET get_balance: bilancio dell'utente
* POST purchase

## Changes
### cambiamenti rispetto all'originale
- corretto PromotionalCustomer con type hinting
- corretto costruttore delle classi customer e aggiunta lista di item a costruttore
- aggiunto metodo per ottenere la lista degli item di un utenrte
- modificata la struttra del progetto in logic e rest
- modificate tutte le path

## TODO
- aggiungere tutti i controlli e le risposte
- probabilmente fare un parser da modello a oggetto python