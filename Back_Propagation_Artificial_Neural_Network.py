#writen by thippo
#python version 3.4.3

class Back_Propagation_Artificial_Neural_Network():
    
    import random
    import math
    import pickle
    import numpy as np
    import matplotlib.pyplot as plt

    def __init__(self,input_layer_nodes,hidden_layer_nodes,output_layer_nodes=1):
        self.input_layer_nodes=input_layer_nodes
        self.hidden_layer_nodes=hidden_layer_nodes
        self.output_layer_nodes=output_layer_nodes
        self.W_hidden=self.np.mat(self.np.random.rand(self.hidden_layer_nodes,self.input_layer_nodes))
        self.B_hidden=self.np.mat(self.np.random.rand(self.hidden_layer_nodes,self.output_layer_nodes))
        self.W_output=self.np.mat(self.np.random.rand(self.output_layer_nodes,self.hidden_layer_nodes))
        self.B_output=self.np.mat(self.np.random.rand(1,1))
        self.global_error_list=[]

    def logsig(self,n):
        return 1/(1+self.math.e**(-n))
       
    def compute_global_error(self):
        global_error=0.0
        for i in self.true_set:
            input_value=self.np.mat(i).T
            A_hidden=self.W_hidden*input_value+self.B_hidden
            for j in range(self.hidden_layer_nodes):
                A_hidden.put(j,self.logsig(float(A_hidden.take(j).getA())))
            A_output=self.W_output*A_hidden+self.B_output
            for j in range(self.output_layer_nodes):
                A_output.put(j,self.logsig(float(A_output.take(j).getA()))) 
            e=1-float(A_output.take(0).getA())
            global_error=global_error+e**2
        for i in self.false_set:
            input_value=self.np.mat(i).T
            A_hidden=self.W_hidden*input_value+self.B_hidden
            for j in range(self.hidden_layer_nodes):
                A_hidden.put(j,self.logsig(float(A_hidden.take(j).getA())))
            A_output=self.W_output*A_hidden+self.B_output
            for j in range(self.output_layer_nodes):
                A_output.put(j,self.logsig(float(A_output.take(j).getA()))) 
            e=0-float(A_output.take(0).getA())
            global_error=global_error+e**2
        return global_error/(2*len(self.true_set)+len(self.false_set))
        
    def learn(self,true_set,false_set,learn_times=5000,alpha=0.1,compute_error=False):
        assert isinstance(true_set,(tuple,list)) and len(true_set[0])==self.input_layer_nodes, 'true_set error'
        assert isinstance(false_set,(tuple,list)) and len(false_set[0])==self.input_layer_nodes, 'false_set error'
        self.true_set=true_set
        self.false_set=false_set
        if compute_error:
            self.global_error_list.append(self.compute_global_error())
        for i in range(learn_times):
            print('Learning times: '+str((i+1))+'/'+str(learn_times))
            if self.random.randint(0,1)==1:
                input_value=self.np.mat(true_set[self.random.randint(0,len(self.true_set)-1)]).T
                expected_value=1.0
            else:
                input_value=self.np.mat(false_set[self.random.randint(0,len(self.false_set)-1)]).T
                expected_value=0.0
            A_hidden=self.W_hidden*input_value+self.B_hidden
            for j in range(self.hidden_layer_nodes):
                A_hidden.put(j,self.logsig(float(A_hidden.take(j).getA())))
            A_output=self.W_output*A_hidden+self.B_output
            for j in range(self.output_layer_nodes):
                A_output.put(j,self.logsig(float(A_output.take(j).getA())))  
            s_output=-2*(expected_value-float(A_output.take(0).getA()))*(1-float(A_output.take(0).getA()))*float(A_output.take(0).getA())
            A_square=self.np.mat(self.np.zeros((self.hidden_layer_nodes,self.hidden_layer_nodes)))
            for j in range(self.hidden_layer_nodes):
                A_square.put(j*(self.hidden_layer_nodes+1),float(A_hidden.take(j).getA())*(1-float(A_hidden.take(j).getA())))
            s_hidden=float(s_output)*A_square*self.W_output.T
            self.W_output=self.W_output-alpha*s_output*A_hidden.T
            self.B_output=self.B_output-alpha*s_output
            self.W_hidden=self.W_hidden-alpha*s_hidden*input_value.T
            self.B_hidden=self.B_hidden-alpha*s_hidden
            if compute_error:
                self.global_error_list.append(self.compute_global_error())
        self.pickle.dump((self.input_layer_nodes,self.hidden_layer_nodes,self.output_layer_nodes),open('layer_nodes.pkl', 'wb'))
        self.pickle.dump(self.global_error_list,open('global_error.pkl', 'wb'))
        self.pickle.dump(self.W_hidden,open('W_hidden.pkl', 'wb'))
        self.pickle.dump(self.B_hidden,open('B_hidden.pkl', 'wb'))
        self.pickle.dump(self.W_output,open('W_output.pkl', 'wb'))
        self.pickle.dump(self.B_output,open('B_output.pkl', 'wb'))
        if compute_error:
            self.plt.plot(range(0,learn_times+1),self.global_error_list)
            self.plt.title("The convergence curve of global error")
            self.plt.xlabel("Learning times")
            self.plt.ylabel("Global error")
            self.plt.savefig('global_error.pdf')
            self.plt.show()
            self.plt.clf()

    def predict(self,true_set,false_set):
        np_total=0;nn_total=0
        np_true=0;nn_false=0
        fout_predict=open('predict_result.th','w')
        for i in true_set:
            np_total=np_total+1
            input_value=self.np.mat(i).T
            A_hidden=self.W_hidden*input_value+self.B_hidden
            for j in range(self.hidden_layer_nodes):
                A_hidden.put(j,self.logsig(float(A_hidden.take(j).getA())))
            A_output=self.W_output*A_hidden+self.B_output
            for j in range(self.output_layer_nodes):
                A_output.put(j,self.logsig(float(A_output.take(j).getA())))
            fout_predict.write(str(float(A_output.take(0).getA()))+'    T\n')
            if float(A_output.take(0).getA())>0.5:
                np_true=np_true+1
        for i in false_set:
            nn_total=nn_total+1
            input_value=self.np.mat(i).T
            A_hidden=self.W_hidden*input_value+self.B_hidden
            for j in range(self.hidden_layer_nodes):
                A_hidden.put(j,self.logsig(float(A_hidden.take(j).getA())))
            A_output=self.W_output*A_hidden+self.B_output
            for j in range(self.output_layer_nodes):
                A_output.put(j,self.logsig(float(A_output.take(j).getA()))) 
            fout_predict.write(str(float(A_output.take(0).getA()))+'    F\n')
            if float(A_output.take(0).getA()) < 0.5:
                nn_false=nn_false+1
        print('predict accuracy rate: '+str((np_true+nn_false)/(np_total+nn_total)))
    



if __name__=='__main__':
    t=[[1,1,1,1,1,-1,-1,-1,-1,-1],[1,-1,1,1,1,-1,-1,-1,-1,-1],[1,1,-1,1,1,-1,-1,-1,-1,-1],[1,1,1,-1,1,-1,-1,-1,-1,-1],[1,1,1,1,-1,-1,-1,-1,-1,-1]]
    f=[[-1,-1,-1,-1,-1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1,1,1,1,1],[-1,-1,-1,-1,-1,1,-1,1,1,1],[-1,-1,-1,-1,-1,1,1,-1,1,1],[-1,-1,-1,-1,-1,1,1,1,-1,1]]
    a=Back_Propagation_Artificial_Neural_Network(10,5,1)
    a.learn(t,f,learn_times=500,alpha=0.1,compute_error=True)
    a.predict(t,f)