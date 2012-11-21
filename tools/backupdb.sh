#!/bin/bash
pg_dump -f "sinq."`date '+%Y-%m-%d-%H-%M-%S'`".db" -F p -U sinq sinq
