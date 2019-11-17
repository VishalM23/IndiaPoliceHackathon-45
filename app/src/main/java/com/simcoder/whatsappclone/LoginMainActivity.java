package com.simcoder.whatsappclone;

import android.app.ProgressDialog;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class LoginMainActivity extends AppCompatActivity {


    private FirebaseAuth auth;
    private EditText mailID;
    private EditText password;
    private Button login;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_main);

        mailID = findViewById(R.id.mailID_new);
        password = findViewById(R.id.password_new);
        login = findViewById(R.id.login);


        auth = FirebaseAuth.getInstance();
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                signin(mailID, password);
            }
        });

    }


    public void signin(EditText mailID, EditText password){
        final ProgressDialog progressDialog=new ProgressDialog(LoginMainActivity.this);
        progressDialog.show();
        auth.signInWithEmailAndPassword(mailID.getText().toString(),password.getText().toString())
                .addOnCompleteListener(this, new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        progressDialog.dismiss();
                        if(task.isSuccessful()){

                        }
                        else {
                            Toast.makeText(getApplicationContext(), "wrong credentials", Toast.LENGTH_LONG).show();
                        }
                    }
                });

    }
}
