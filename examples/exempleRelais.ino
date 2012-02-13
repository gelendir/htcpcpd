// vim: set syntax=arduino:

const int PIN_RELAY = 5;

void setup() {

    Serial.begin(9600);
    pinMode( PIN_RELAY, OUTPUT );
    digitalWrite( PIN_RELAY, LOW );
    Serial.println("Booted");
    Serial.println("Press 1 to turn on relay, 0 to turn off");

}

void loop() {

    if( Serial.available() ) {

        char character = Serial.read();
        if( character == '0' ) {
            digitalWrite( PIN_RELAY, LOW );
        } else if ( character == '1' ) {
            digitalWrite( PIN_RELAY, HIGH );
        }

    }

}
