// AGSMultiplayer.cpp
// This is the an engine plugin for Adventure Game Studio to enable multiplayer
// Copyright (c) 2013 Lara Martin

#include "stdafx.h"
#include "AGSMultiplayer.h"

#define WIN32_LEAN_AND_MEAN
#include <windows.h>

#define THIS_IS_THE_PLUGIN
#include "agsplugin.h"

#include <SFML/Network.hpp>
using namespace sf;
#include <string>

#pragma unmanaged
BOOL APIENTRY DllMain( HANDLE hModule, 
	DWORD  ul_reason_for_call, 
	LPVOID lpReserved) {

		switch (ul_reason_for_call)	{
		case DLL_PROCESS_ATTACH:
		case DLL_THREAD_ATTACH:
		case DLL_THREAD_DETACH:
		case DLL_PROCESS_DETACH:
			break;
		}
		return TRUE;
}
#pragma managed

// ***** DESIGN TIME CALLS *******
IAGSEditor *editor;

const char *ourScriptHeader =
	"import void SendData(char*, unsigned short);\r\n"
	"import int ReceiveData(char*, std::size_t, unsigned short);\r\n"
	"import std::string getFriendIP(void);\r\n"
	"import void setFriendIP(const std::string &);\r\n";

LPCSTR AGS_GetPluginName(void) {
	// Return the plugin description
	return "Network Multiplayer Plugin";
}

int  AGS_EditorStartup (IAGSEditor *lpEditor) {
	// User has checked the plugin to use it in their game

	// If it's an earlier version than what we need, abort.
	if (lpEditor->version < 1)
		return -1;

	editor = lpEditor;
	editor->RegisterScriptHeader (ourScriptHeader);

	// Return 0 to indicate success
	return 0;
}

void AGS_EditorShutdown () {
	// User has un-checked the plugin from their game
	editor->UnregisterScriptHeader (ourScriptHeader);
}

void AGS_EditorProperties (HWND parent) {
	// User has chosen to view the Properties of the plugin
	// We could load up an options dialog or something here instead
	//MessageBox(parent, "Multiplayer Plugin, copyright (c) 2013 Lara Martin", "About", MB_OK | MB_ICONINFORMATION);
}

int AGS_EditorSaveGame (char *buffer, int bufsize) {
	// We don't want to save any persistent data
	return 0;
}

void AGS_EditorLoadGame (char *buffer, int bufsize) {
	// Nothing to load for this dummy plugin
}

// ******* END DESIGN TIME  *******


// ****** RUN TIME ********

IAGSEngine *engine;
sf::IpAddress myIP = sf::IpAddress::LocalHost;
sf::IpAddress friendIP;

// Your address in the world wide web (like 83.2.124.68 -- the one you get with www.whatismyip.org)
sf::IpAddress myWebIP = sf::IpAddress::getPublicAddress();

std::string getFriendIP(void)
{
	return friendIP.toString();
}
void setFriendIP(const std::string & IP)
{
	friendIP = IpAddress(IP);
}

int SendData(char data[1000], unsigned short port)
{
	// Create the UDP socket
	sf::UdpSocket Socket;

	//UDP socket
	//send (Packet &packet, const IpAddress &remoteAddress, unsigned short remotePort)
	if (friendIP == sf::IpAddress::None)
	{
		if (Socket.send(data, sizeof(data), friendIP, port) != sf::Socket::Done)
		{
			//Socket.unbind();
			return -1;
		}
		//Socket.unbind();
		return 0;
	}
	//Socket.unbind();
	return -1;
}

int ReceiveData(char data[1000], std::size_t received, unsigned short port)
{
	// Create the UDP socket
	sf::UdpSocket Socket;

	//bind it
	if (Socket.bind(port) != sf::Socket::Done)
	{
		Socket.unbind();
		return -1;
	}

	//UDP socket
	//receive (Packet &packet, IpAddress &remoteAddress, unsigned short &remotePort)
	if (Socket.receive(data, sizeof(data), received, friendIP, port) != sf::Socket::Done)
	{
		Socket.unbind();
		return -1;
	}
	//std::cout << "Received from " << friendIP << " on port " << port << std::endl;
	Socket.unbind();
	return 0;
}

void AGS_EngineStartup (IAGSEngine *lpEngine) {
	engine = lpEngine;

	// Make sure it's got the version with the features we need
	if (engine->version < 3) {
		engine->AbortGame ("Engine interface is too old. You need a newer version of AGS.");
	}

	engine->RegisterScriptFunction ("SendData", SendData);
	engine->RegisterScriptFunction ("ReceiveData", ReceiveData);
	engine->RegisterScriptFunction ("setFriendIP", setFriendIP);
	engine->RegisterScriptFunction ("getFriendIP", getFriendIP);
	engine->RequestEventHook (AGSE_SAVEGAME);
}

void AGS_EngineShutdown() {
	// no work to do here - but if we had created any dynamic sprites,
	// we should delete them here
}

int AGS_EngineOnEvent (int event, int data) {
	//events are AGSE_*
	if (event == AGSE_SAVEGAME) {
    /*
    long screenWidth, colDepth, a;
    // Get a reference to the screen we'll draw onto
    BITMAP *virtsc = engine->GetVirtualScreen();
    // Get its surface, in both 8-bit and 16-bit flavours
    unsigned char **charbuffer = engine->GetRawBitmapSurface (virtsc);
    unsigned short **shortbuffer = (unsigned short**)charbuffer;

    // Find out the screen width and colour depth
    engine->GetScreenDimensions (&screenWidth, NULL, &colDepth);

    // Draw a bright blue line across the screen near the top
    for (a = 0; a < screenWidth; a++) {
      if (colDepth <= 8)
        charbuffer[20][a] = 10;
      else if (colDepth <= 16)
        shortbuffer[20][a] = 32155;
      else  // I've been lazy, and haven't implemented 24/32-bit
        engine->AbortGame("This plugin does not support 32-bit graphics");
    }

    // Release the screen so that the engine can continue
    engine->ReleaseBitmapSurface (virtsc);*/
  }
  return 0;
}

// *** END RUN TIME ****
