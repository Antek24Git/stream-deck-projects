#include <IRremote.h>

const int RECV_PIN = 7;
IRrecv irrecv(RECV_PIN);
decode_results results;
unsigned long key_value = 0;
void setup(){
  Serial.begin(9600);
  irrecv.enableIRIn();
  irrecv.blink13(true);
}

void loop(){
  if (irrecv.decode(&results)){
        if (results.value == 0XFFFFFFFF)
          results.value = key_value;

        switch(results.value){
          case 0xFFA25D:
          Serial.println("1");
          break;
          case 0xFF629D:
          Serial.println("2");
          break;
          case 0xFFE21D:
          Serial.println("3");
          break;
          case 0xFF22DD:
          Serial.println("4");
          break;
          case 0xFF02FD:
          Serial.println("5");
          break ;
          case 0xFFC23D:
          Serial.println("6");
          break ;
          case 0xFFE01F:
          Serial.println("7");
          break ;
          case 0xFFA857:
          Serial.println("8");
          break ;
          case 0xFF906F:
          Serial.println("9");
          break ;
          case 0xFF6897:
          Serial.println("10");
          break ;
          case 0xFF9867:
          Serial.println("11");
          break ;
          case 0xFFB04F:
          Serial.println("12");
          break ;
          case 0xFF30CF:
          Serial.println("13");
          break ;
          case 0xFF18E7:
          Serial.println("14");
          break ;
          case 0xFF7A85:
          Serial.println("15");
          break ;
          case 0xFF10EF:
          Serial.println("16");
          break ;
          case 0xFF38C7:
          Serial.println("17");
          break ;
          case 0xFF5AA5:
          Serial.println("18");
          break ;
          case 0xFF42BD:
          Serial.println("19");
          break ;
          case 0xFF4AB5:
          Serial.println("20");
          break ;
          case 0xFF52AD:
          Serial.println("21");
          break ;
        }
        key_value = results.value;
        delay(500);
        irrecv.resume();
          
  }
}
