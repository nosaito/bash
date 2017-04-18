@echo off

::
::if using following option, args need to be !arg! instead of %arg%
:: setlocal enabledelayedexpansion
::

:: chdir to the directory this script placed on
cd /d %~dp0
: or pushd %0\..

set HOGE="test"

::---------------------
:: comment
:: main
::---------------------


rem comment


: check args

set HOGE="none"
:ARG_LOOP
    if "%1"=="" goto :ARG_LOOP_END
    if "%1"=="hello" echo "hello world"
    if "%1"=="1" set HOGE="hoge1"
    if "%1"=="2" set HOGE="hoge2"
    if "%1"=="3" set HOGE="hoge3"
    shift
    goto :ARG_LOOP
:ARG_LOOP_END


echo test %HOGE%

call :msgprint ore1 ore2

:pause
exit


:---------------------
: subroutine
:---------------------


:msgprint
  echo test2 %1 %2 %3
  exit /b
