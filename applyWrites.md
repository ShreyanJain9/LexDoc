# com.atproto.repo.applyWrites
## 

Apply a batch transaction of creates, updates, and deletes.

**Type**: procedure

### Input

**Encoding**: application/json

#### Schema

### Parameters

**repo**: *string*
string
The handle or DID of the repo.

**validate**: *boolean*
boolean
Validate the records?

**writes**: *array*
array of #create or #update or #delete


**swapCommit**: *string*
string


### Errors

**InvalidSwap**: 

## create

Create a new record.

**Type**: object

### Properties

**collection**: *string*
string


**rkey**: *string*
string


**value**: *unknown*
unknown


## update

Update an existing record.

**Type**: object

### Properties

**collection**: *string*
string


**rkey**: *string*
string


**value**: *unknown*
unknown


## delete

Delete an existing record.

**Type**: object

### Properties

**collection**: *string*
string


**rkey**: *string*
string



