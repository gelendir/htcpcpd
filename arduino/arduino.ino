// vim: set syntax=arduino:

/*
 * General pins
 */
const int PIN_BOILER = 8;
const int PIN_POT = 7;

/*
 * Water pins
 */
struct WaterPin {
    const int pin;
    const int nbLiters;
    const int minReading;
};

const int NB_WATER_PINS = 4;

const struct WaterPin WATER_PINS[] = {
    { A0, 1, 10 },
    { A1, 4, 10 },
    { A2, 8, 10 },
    { A3, 12, 10 }
};

/*
 * Commands
 */
const char COMMAND_BREW_COFFEE[]        PROGMEM = "BREW DIS COFFEE PLZ";
const char COMMAND_BREWING_STATE[]      PROGMEM = "AR U BREWING COFFEEZ ?";
const char COMMAND_WATER_QUANTITY[]     PROGMEM = "I CAN HAZ MOAR WATER ?";
const char COMMAND_POT_PRESENCE[]       PROGMEM = "O HAI! I WAN MAH BUKKET ! U HAZ BUKKET ?";
const char COMMAND_STOP_BREWING[]       PROGMEM = "OUCH OUCH! TIZ COFFEE IZ HAWT! STOP!";
const char COMMAND_WATER_READING[]      PROGMEM = "WATER READING";
const char COMMAND_TIME_LEFT[]          PROGMEM = "TIME LEFT";

/* Responses */
const char RESPONSE_STR_POT_AVAILABLE[]             PROGMEM = "I HAZ YUR BUKKET";
const char RESPONSE_STR_POT_NOT_AVAILABLE[]         PROGMEM = "I AINT HAZ NO BUKKET";
const char RESPONSE_STR_WATER_QUANTITY[]            PROGMEM = "I HAZ % LEETEARZ";
const char RESPONSE_STR_NO_WATER_LEFT[]             PROGMEM = "OE NOES !1! NO MOAR WATERZ";
const char RESPONSE_STR_BREWING[]                   PROGMEM = "I'M BREWING COFFEEZ";
const char RESPONSE_STR_NOT_BREWING[]               PROGMEM = "I AIN'T BREWING COFFEEZ";
const char RESPONSE_STR_STARTED_BREWING[]           PROGMEM = "YES DIS COFFEE POT IZ BREWINGZ";
const char RESPONSE_STR_ALREADY_BREWING[]           PROGMEM = "I HAZ ALREADY COFFEE A BREWING";
const char RESPONSE_STR_STOPPED_BREWING[]           PROGMEM = "COFFEE IZ STOP";
const char RESPONSE_STR_CANNOT_STOP_BREWING[]       PROGMEM = "NO COFFEE BREWIN";

struct Response {
    const int code;
    const char* message;
};

struct Response RESPONSE_POT_AVAILABLE = {
    200,
    RESPONSE_STR_POT_AVAILABLE
};

struct Response RESPONSE_POT_NOT_AVAILABLE = {
    404,
    RESPONSE_STR_POT_NOT_AVAILABLE
};

struct Response RESPONSE_WATER_QUANTITY = {
    200,
    RESPONSE_STR_WATER_QUANTITY
};

struct Response RESPONSE_NO_WATER_LEFT = {
    400,
    RESPONSE_STR_NO_WATER_LEFT
};

struct Response RESPONSE_NOT_BREWING = {
    210,
    RESPONSE_STR_NOT_BREWING
};

struct Response RESPONSE_BREWING = {
    220,
    RESPONSE_STR_BREWING
};

struct Response RESPONSE_STARTED_BREWING = {
    200,
    RESPONSE_STR_STARTED_BREWING
};

struct Response RESPONSE_ALREADY_BREWING = {
    500,
    RESPONSE_STR_ALREADY_BREWING
};

struct Response RESPONSE_STOPPED_BREWING = {
    200,
    RESPONSE_STR_STOPPED_BREWING
};

struct Response RESPONSE_CANNOT_STOP_BREWING = {
    400,
    RESPONSE_STR_CANNOT_STOP_BREWING
};

/*
 * Other constants
 */
const char NEWLINE = '\n';
const long TIMER_MAX_MILLISECS = 12L * 60L * 1000L;

/*
 *Global variables
 */
bool boilerOn = false;
long boilerTimestamp = 0;

/*
 * prototypes
 */
String readCommand();
boolean isCommand( String input, const char* command );
boolean isPotPresent();
void sendResponse();
int nbWaterLiters();
void processPotState();
void processWaterQuantity();
void processStartBrewing();
void processStopBrewing();
void checkBoilerTimer();

/*
 * Main program
 */
void setup() {

    Serial.begin(9600);

    //setup pot pin as input mode with interal pull-down resistor
    pinMode( PIN_POT, INPUT );
    digitalWrite( PIN_POT, LOW );

    //setup boiler pin as output
    pinMode( PIN_BOILER, OUTPUT );

    //setup water pins as input
    for( int i = 0; i < NB_WATER_PINS; i++ ) {
        pinMode( WATER_PINS[i].pin, INPUT );
    }

    //Serial.println("BOOTED");
}

void loop() {

    checkBoilerTimer();

    if( Serial.available() ) {

        String command = readCommand();

        if( isCommand( command, COMMAND_POT_PRESENCE ) ) {
            processPotPresence();
        } else if ( isCommand( command, COMMAND_WATER_QUANTITY ) ) {
            processWaterQuantity();
        } else if( isCommand( command, COMMAND_BREWING_STATE ) ) {
            processBrewingState();
        } else if( isCommand( command, COMMAND_BREW_COFFEE ) ) {
            processStartBrewing();
        } else if ( isCommand( command, COMMAND_STOP_BREWING ) ) {
            processStopBrewing();
        } else if ( isCommand( command, COMMAND_WATER_READING ) ) {
            processWaterReadings();
        } else if ( isCommand( command, COMMAND_TIME_LEFT ) ) {
            processTimeLeft();
        }
        

    }

}

/**
 * This method read a command from the serial port and
 * return the line without the new line character. Each
 * command end by the new line character.
 * @return Return the received command without the new 
 * line character.
 */
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

/**
 * This method verify if the line received from the serial
 * port fit with the command passed in parameter.
 * @param[in] input The command received from the serial port
 * @param[in] command The command for comparison
 * @return Return true if the two parameters a equals; false 
 * otherwise.
 */
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

/**
 * This method verify if the pot is present.
 * @return Return true if the pot is present; false otherwise.
 */
boolean isPotPresent() {

    boolean state = digitalRead( PIN_POT );
    return state;

}

/**
 * This method return the number of litres there is in the
 * recipient of the coffee pot.
 * @return Return the number of litres there is in the
 * recipient of the coffee pot.
 */
int nbWaterLiters() {

    int liters = 0;
    bool on = true;

    for( int i = 0; i < NB_WATER_PINS && on; ++i ) {

        int value = analogRead( WATER_PINS[i].pin );
        on = ( value >= WATER_PINS[i].minReading );

        if( on ) {
            liters = WATER_PINS[i].nbLiters;
        }
    }

    return liters;

}

/**
 * This method send the response in the serial port.
 * @param[in] response The response to send
 * @param[in] arg A number to print in the response. The presence
 * of this number in the response is set by % in the response.
*/
void sendResponse( struct Response response, int arg = 0 ) {

    const char* message = response.message;

    Serial.print( response.code );
    Serial.print(" ");

    char character = (char)pgm_read_byte( message );
    while( character != '\0' ) {

        if( character == '%' ) {
            Serial.print( arg );
        } else {
            Serial.print( character );
        }

        message++;
        character = (char)pgm_read_byte( message );
    }

    Serial.println();

}

/**
 * This method send to the serial port the response
 * of the command to know if the pot is present or not.
 */
void processPotPresence() {

    if( isPotPresent() ) {
        sendResponse( RESPONSE_POT_AVAILABLE );
    } else {
        sendResponse( RESPONSE_POT_NOT_AVAILABLE );
    }

}

/**
 * This method send to the serial port the response
 * of the command to know the quantity of the water.
 */
void processWaterQuantity() {

    int liters = nbWaterLiters();
    if( liters == 0 ) {
        sendResponse( RESPONSE_NO_WATER_LEFT );
    } else {
        sendResponse( RESPONSE_WATER_QUANTITY, liters );
    }

}

/**
 * This method send to the serial port the response
 * of the command to know the brewing state.
 */
void processBrewingState() {

    if( boilerOn ) {
        sendResponse( RESPONSE_BREWING );
    } else {
        sendResponse( RESPONSE_NOT_BREWING );
    }

}

/**
 * This method check if the number of litre in the recipient
 * is zero or if the heating time exceeds a certain time. If yes,
 * The boiler is stopped.
 */
void checkBoilerTimer() {

    if( boilerOn ) {

        long currentTimestamp = millis();
        int liters = nbWaterLiters();

        if( liters == 0 ||
            currentTimestamp >= boilerTimestamp + TIMER_MAX_MILLISECS
        ) {
            stopBoiler();
        } else {
        }

    }

}

/**
 * This method start the boiler of the coffee pot.
 */
void startBoiler() {

    digitalWrite( PIN_BOILER, HIGH );
    boilerTimestamp = millis();
    boilerOn = true;

}

/**
 * This method stop the boiler of the coffee pot.
 */
void stopBoiler() {

    digitalWrite( PIN_BOILER, LOW );
    boilerTimestamp = 0;
    boilerOn = false;

}

/**
 * This method send to the serial port the response
 * of the command to start the boiler.
 */
void processStartBrewing() {

    if( boilerOn ) {
        sendResponse( RESPONSE_ALREADY_BREWING );
    } else if ( nbWaterLiters() == 0 ) {
        sendResponse( RESPONSE_NO_WATER_LEFT );
    } else {
        startBoiler();
        sendResponse( RESPONSE_STARTED_BREWING );
    }

}

/**
 * This method send to the serial port the response
 * of the command to stop the boiler.
 */
void processStopBrewing() {

    if( !boilerOn ) {
        sendResponse( RESPONSE_CANNOT_STOP_BREWING );
    } else {
        stopBoiler();
        sendResponse( RESPONSE_STOPPED_BREWING );
    }

}

void processWaterReadings() {
  for(int i = 0; i < NB_WATER_PINS; ++i) {
    Serial.print(i);
    Serial.print(": ");
    Serial.print(analogRead(WATER_PINS[i].pin));
    Serial.print(" ");
  }
  Serial.println();
}

void processTimeLeft() {
  Serial.println(millis() - boilerTimestamp);
}

