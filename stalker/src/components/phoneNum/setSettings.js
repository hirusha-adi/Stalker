import React from 'react';
import TextField from '@mui/material/TextField';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import DeleteIcon from '@mui/icons-material/Delete';
import Stack from '@mui/material/Stack';
import SaveIcon from '@mui/icons-material/Save';

const FormItems = () => (
    <React.Fragment>
        <Grid container spacing={1}>
            <Grid container item spacing={3}>
                <Grid item>
                    <TextField id="standard-basic" label="NUMVERIFY_API_KEY" variant="standard" fullWidth />
                </Grid>
                <Grid item>
                    <TextField id="standard-basic" label="GOOGLECSE_CX" variant="standard" fullWidth />
                </Grid>
                <Grid item>
                    <TextField id="standard-basic" label="GOOGLE_API_KEY" variant="standard" fullWidth />
                </Grid>
            </Grid>
        </Grid>
    </React.Fragment>
);

const setSettings = () => {
    return (
        <Paper elevation={3} sx={{ p: 2, display: 'flex', alignItems: 'center', justifyContent: 'center' }} >
            <div>
                <h2>Update Settings</h2>
                <FormItems />
                <br></br>
                <Stack direction="row" spacing={2} sx={{ p: 2, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <Button variant="outlined" color="error" startIcon={<DeleteIcon />}>
                        Clear
                    </Button>
                    <Button variant="contained" endIcon={<SaveIcon />}>
                        Update
                    </Button>
                </Stack>
            </div>
        </Paper>
    );
}

export default setSettings;