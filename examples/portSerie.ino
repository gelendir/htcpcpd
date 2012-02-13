void setup() {

    //Ouvrir le port série et ajuster le "baud-rate"
    Serial.begin(9600);
    //Avertir l'utilisateur que l'arduino est prêt à recevoir des strings
    Serial.println("Booted");
}

String message;

void loop() {

    //Vérification si nous avons reçu des données
    while( Serial.available() ) {

        char in = Serial.read();

        //Debug, vérification des charactères reçus
        Serial.print("Character is ");
        Serial.println(in);

        //Nous utilisons le retour de chariot pour indiquer
        //la fin de la chaîne de charactères
        if( in == '\n' ) {
            Serial.println(message);
            message = "";
        } else {
            //Vu que Serial.read() retourne seulement un
            //charactère à la fois, nous avons besoin de les accumuler
            message.concat( in );
        }

    }

}
