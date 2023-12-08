import React from 'react';
import TextField from '@mui/material/TextField';

const setSettings = () => {
    return (
        <div>
            <h2>Set Your Settings</h2>
            <TextField id="standard-basic" label="Standard" variant="standard" />
        </div>
    );
}

export default setSettings;