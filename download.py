import air_download.air_download as air
import argparse

args = argparse.Namespace()
args.cred_path = '../../air_login.txt'
args.URL       = 'https://air.radiology.ucsf.edu/api/'
args.acc       = '10023990293'
args.profile   = -1
args.output    = '10023990293.zip'

air.main(args)