// vim: set syntax=arduino:

/*
 * General pins
 */
const int PIN_BOILER = 0;
const int PIN_POT = 1;

/*
 * Water pins
 */
const int PIN_4L = 2;
const int PIN_8L = 3;
const int PIN_12L = 4;

const int NB_WATER_PINS = 3;

const int WATER_PINS[NB_WATER_PINS] = { PIN_4L, PIN_8L, PIN_12L };

/*
 * Commands
 */
const char COMMAND_BREW_COFFEE[]    PROGMEM = "BREW DIS COFFEE PLZ";
const char COMMAND_POT_STATE[]      PROGMEM = "O HAI! I WAN MAH BUKKET ! U HAZ BUKKET ?";
const char COMMAND_WATER_QUANTITY[] PROGMEM = "I CAN HAZ MOAR WATER ?";
const char COMMAND_POT_PRESENCE[]   PROGMEM = "O HAI! I WAN MAH BUKKET ! U HAZ BUKKET ?";
const char COMMAND_STOP_BREWING[]   PROGMEM = "OUCH OUCH! TIZ COFFEE IZ HAWT! STOP!";

/* Responses */

struct Response {
    const int code;
    const char* PROGMEM message;
};

struct Response RESPONSE_POT_AVAILABLE = {
    200,
    "I AIN'T BREWING COFFEEZ"
};

struct Response RESPONSE_POT_NOT_AVAILABLE = {
    210,
    "I'M BREWING COFFEEZ"
};

/*
 * Other constants
 */
const char NEWLINE = '\n';

/*
 *Global variables
 */
bool boilerOn = false;

/*
 * prototypes
 */
String readCommand();
boolean isCommand( String input, const char* command );
boolean isPotPresent();
void sendResponse();
void processPotState();

void setup() {
    Serial.begin(9600);
    Serial.println("booted");
}

void loop() {

    if( Serial.available() ) {

        String command = readCommand();
        if( isCommand( command, COMMAND_POT_STATE ) ) {
            processPotState();
        }

    }

}

String readCommand() {

    String command = "";
    bool endOfCommand = false;

    char in = '\0';

    while( !endOfCommand ) {

        while( Serial.available() ) {
            in = Serial.read();
            if( in == NEWLINE ) {
                endOfCommand = true;
            } else {
                command.concat(in);
            }
        }

    }

    return command;
}

boolean isCommand( String input, const char* command ) {

    byte pos = 0;
    boolean same = true;
    char character = (char)pgm_read_byte(command);

    while ( same && character != '\0' ) {

        same = ( character == input[pos] );

        command++;
        pos++;
        character = (char)pgm_read_byte(command);
    }

    return same;

}

boolean isPotPresent() {

    boolean state = digitalRead( PIN_POT );
    return state;

}

void sendResponse( struct Response response  ) {

    const char* message = response.message;

    Serial.print( response.code );
    Serial.print(" ");

    char character = (char)pgm_read_byte( message );
    while( character != '\0' ) {
        Serial.print( character );
        message++;
        character = (char)pgm_read_byte( message );
    }

    Serial.println();

}

void processPotState() {

    if( isPotPresent() ) {
        sendResponse( RESPONSE_POT_AVAILABLE );
    } else {
        sendResponse( RESPONSE_POT_NOT_AVAILABLE );
    }

}

