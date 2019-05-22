#pragma once

#include <stdlib.h>
#include <ctime>

#include "lib/script.h"
#include "lib/utils.h"

#include "lib/rapidjson/document.h"
#include "lib/rapidjson/stringbuffer.h"

#include "ScreenCapturer.h"
#include "Rewarders\Rewarder.h"

using namespace rapidjson;

//#define DEBUG 1

class Scenario {
private:
	static char* weatherList[14];

	
	

	Vehicle vehicle = NULL;
	Vehicle vehicle2 = NULL;
	Vehicle vehicle3 = NULL;
	Vehicle vehicle4 = NULL;

	Player player = NULL;
	Ped ped = NULL;
	Cam camera = NULL;
	Vector3 dir;
	Vector3 CurrentPklot;
	int px, py, pz;
	int j;

	float x, y;
	int hour, minute;
	const char* _weather;

	int width, height;

	bool vehicles;
	bool peds;
	bool trafficSigns; //TODO
	bool direction;
	bool reward;
	bool throttle;
	bool brake;
	bool steering;
	bool speed;
	bool yawRate;
	bool drivingMode; //TODO
	bool location;
	bool time;

	float currentThrottle = 0.0;
	float currentBrake = 0.0;
	float currentSteering = 0.0;

	Rewarder* rewarder;
	std::clock_t lastSafetyCheck;
	int _drivingMode;
	float _setSpeed;

	bool running = false;
	Document d;

public:
	int rate;
	static char* vehicleList[13];
	char* _vehicle;
	Vehicle myvehicles[200];
	Vehicle vehicletemp;
	float rowx[12] = { -1643.68,-1647.39,-1656.49,-1659.88,-1669,-1672.78 ,-1704.63,-1700.52,-1691.55,-1687.93,-1678.66,-1674.72 };
	float rowy[12] = { -877.637,-882.065,-892.894,-897,-907.143,-911.851 ,-885.067,-880.115,-869.744,-865.654,-855.002,-850.478 };

	char mytext[10];

	char* mymodel;
	int mymodelnum;
	int myrow;
	int myplace;
	int myside;
	int mycolor;
	int nbcar=0;

	bool iscar = false;
	bool test = false;

	void GenerateRandomCar();
	void GenerateMyCar(int row, int place, int side, char* model,float heading,int color,unsigned int num,int modelnum);
	void parseCarConfig(const Value& cc);
	void setCamera(const Value& sc);
	void isCar(const Value& ic);
	void PrintMessage(char* message);
	
	void start(const Value& sc, const Value& dc);
	void stop();
	void config(const Value& sc, const Value& dc);
	void setCommands(float throttle, float brake, float steering);
	void run();

	ScreenCapturer* screenCapturer;
	StringBuffer generateMessage();

private:
	

	void parseScenarioConfig(const Value& sc, bool setDefaults);
	void parseDatasetConfig(const Value& dc, bool setDefaults);
	void buildScenario();

	void setVehiclesList();
	void setPedsList();
	void setTrafficSignsList();
	void setDirection();
	void setReward();
	void setThrottle();
	void setBrake();
	void setSteering();
	void setSpeed();
	void setYawRate();
	void setDrivingMode();
	void setLocation();
	void setTime();


	void setMyMessage();
};