echo off

copy .\QtApp\Dialog.ui  Dialog.ui

pyuic5 -o ui_Dialog.py  Dialog.ui