package com.blauhaus.android.redwood.sample

import com.blauhaus.android.redwood.sample.data.IRepository
import com.blauhaus.android.redwood.sample.data.Repository
import com.blauhaus.android.redwood.sample.viewmodels.AchievmentViewModel
import org.koin.dsl.module


val mainModule = module {
    single { Repository() as IRepository }
    single { AchievmentViewModel(get()) }
}
